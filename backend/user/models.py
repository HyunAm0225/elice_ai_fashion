from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from style.models import Style
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
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("User", related_name="user", on_delete=models.CASCADE, db_column='user_id')
    dress_img = models.ImageField(upload_to='%Y/%m/%d')

    class meta:
        db_table = 'closet'
