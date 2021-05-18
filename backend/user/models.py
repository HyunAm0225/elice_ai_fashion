from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField('nickname', max_length=40, default='')
    # 성별 선언해주기
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    CHOICES_GENDER = (
        (GENDER_MALE, '남성'),
        (GENDER_FEMALE, '여성'),
    )
    gender = models.CharField(max_length=10, choices=CHOICES_GENDER, null=True)

    @property
    def name(self):
        return f"{self.last_name}{self.first_name}"

    REQUIRED_FIELDS = ['nickname']

    class meta:
        db_table = 'users'
