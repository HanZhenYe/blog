# Generated by Django 2.2 on 2020-08-24 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20200824_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='title',
        ),
        migrations.AlterField(
            model_name='notice',
            name='content',
            field=models.CharField(max_length=40, verbose_name='内容'),
        ),
    ]