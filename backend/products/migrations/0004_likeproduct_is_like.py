# Generated by Django 3.2.3 on 2021-05-28 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210528_0459'),
    ]

    operations = [
        migrations.AddField(
            model_name='likeproduct',
            name='is_like',
            field=models.BooleanField(default=False),
        ),
    ]
