from django.db import models
from user.models import User

# Create your models here.


class Style(models.Model):
    id = models.AutoField(primary_key=True)
    # user_id = models.ForeignKey(User, related_name="%(class)s_user", on_delete=models.CASCADE)
    style_img = models.ImageField(upload_to='%Y/%m/%d', verbose_name="image_url", default="null")
    feature = models.JSONField(default=dict, blank=True)

    class meta:
        db_table = 'style'
