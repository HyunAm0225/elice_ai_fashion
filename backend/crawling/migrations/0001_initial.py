# Generated by Django 3.2.3 on 2021-05-19 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crawl_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=200)),
                ('sale_price', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('discount_rate', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('img_url', models.CharField(max_length=200)),
            ],
        ),
    ]