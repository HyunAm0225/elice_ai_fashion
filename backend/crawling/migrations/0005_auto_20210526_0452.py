# Generated by Django 3.2.3 on 2021-05-25 19:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crawling', '0004_auto_20210525_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='star',
        ),
        migrations.CreateModel(
            name='LikeProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='like_product', to='crawling.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'likeproducts',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='likeProduct',
            field=models.ManyToManyField(related_name='like_product', through='crawling.LikeProduct', to=settings.AUTH_USER_MODEL),
        ),
    ]
