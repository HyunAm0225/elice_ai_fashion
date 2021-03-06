# Generated by Django 3.2.3 on 2021-06-02 05:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('img_url', models.URLField(max_length=2000, verbose_name='image_url')),
                ('feature', models.JSONField(blank=True, default=dict)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='style_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
