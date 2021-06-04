# Generated by Django 3.2.3 on 2021-06-03 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('style', '0002_auto_20210602_1418'),
        ('user', '0003_auto_20210526_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='styles',
            field=models.ForeignKey(blank=True, db_column='style_id', default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='style', to='style.style'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', '남성'), ('female', '여성')], default='', max_length=10),
        ),
    ]
