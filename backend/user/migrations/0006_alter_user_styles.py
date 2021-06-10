# Generated by Django 3.2.3 on 2021-06-10 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('style', '0002_auto_20210602_1418'),
        ('user', '0005_auto_20210603_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='styles',
            field=models.ManyToManyField(blank=True, db_column='style_id', default='', related_name='style', to='style.Style'),
        ),
    ]