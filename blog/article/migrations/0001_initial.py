# Generated by Django 2.2 on 2020-08-20 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='分类名称')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
                'db_table': 'classification',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='标题')),
                ('creation_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('browse_number', models.IntegerField(verbose_name='浏览量')),
                ('comment_number', models.IntegerField(verbose_name='评论量')),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Classification')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'db_table': 'article',
            },
        ),
    ]
