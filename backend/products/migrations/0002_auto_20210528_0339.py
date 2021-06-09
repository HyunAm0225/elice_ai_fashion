# Generated by Django 3.2.3 on 2021-05-27 18:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likeproduct',
            old_name='products',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='likeproduct',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='likeProduct',
        ),
        migrations.AddField(
            model_name='product',
            name='likeproduct',
            field=models.ManyToManyField(blank=True, related_name='like_product', through='products.LikeProduct', to=settings.AUTH_USER_MODEL),
        ),
    ]