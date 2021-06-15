from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from style.models import Style
from uuid import uuid4
from django.utils import timezone
import os

# Create your models here.


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.CharField(
        max_length=255,
        unique=True
    )
    username = models.CharField(
        'name', max_length=40, unique=False, default='')
    # 성별 선언해주기
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    CHOICES_GENDER = (
        (GENDER_MALE, '남성'),
        (GENDER_FEMALE, '여성'),
    )
    gender = models.CharField(max_length=10, choices=CHOICES_GENDER, blank=True, default='')
    styles = models.ManyToManyField(Style, related_name="style", blank=True, db_column='style_id', default='')

    @property
    def name(self):
        return f"{self.last_name} {self.first_name}"

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    class meta:
        db_table = 'users'


class Closet(models.Model):
    def date_upload_to(self, filename):
        # upload_to="%Y/%m/%d" 처럼 날짜로 세분화
        ymd_path = timezone.now().strftime('%Y/%m/%d')
        # 길이 32 인 uuid 값
        uuid_name = uuid4().hex
        # 확장자 추출
        extension = os.path.splitext(filename)[-1].lower()
        # 결합 후 return
        return '/'.join([
            ymd_path,
            uuid_name + extension,
        ])
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("User", related_name="user", on_delete=models.CASCADE, db_column='user_id')
    dress_img = models.ImageField(upload_to=date_upload_to)
    feature = models.JSONField(default=dict, blank=True)

    class meta:
        db_table = 'closet'
