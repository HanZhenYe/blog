# Generated by Django 2.2 on 2020-08-20 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20200820_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, verbose_name='文章内容'),
        ),
    ]
