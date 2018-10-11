# Generated by Django 2.1.1 on 2018-09-30 12:54

from django.db import migrations, models
import django.db.models.deletion
import imiss.category.model_tool


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lrc', models.FileField(upload_to=imiss.category.model_tool.user_directory_path, verbose_name='歌词')),
                ('mp3', models.FileField(upload_to=imiss.category.model_tool.user_directory_path, verbose_name='音乐')),
            ],
            options={
                'db_table': 'Resource',
            },
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='标题')),
                ('detail', models.CharField(max_length=20, verbose_name='详情')),
                ('img', models.CharField(max_length=20, verbose_name='图片')),
                ('url', models.CharField(max_length=20, verbose_name='跳转链接')),
            ],
            options={
                'db_table': 'Share',
            },
        ),
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='歌单')),
                ('img', models.ImageField(blank=True, null=True, upload_to=imiss.category.model_tool.user_directory_path, verbose_name='图片')),
            ],
            options={
                'db_table': 'Sheet',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='歌名')),
                ('author', models.CharField(max_length=20, verbose_name='作者')),
                ('big_img', models.ImageField(blank=True, null=True, upload_to=imiss.category.model_tool.user_directory_path, verbose_name='大图')),
                ('small_img', models.ImageField(blank=True, null=True, upload_to=imiss.category.model_tool.user_directory_path, verbose_name='小图')),
                ('introduction', models.CharField(max_length=20, verbose_name='介绍')),
                ('detail', models.CharField(max_length=20, verbose_name='详情')),
                ('likeNumber', models.IntegerField(verbose_name='喜欢人数')),
                ('listenNumber', models.IntegerField(verbose_name='听歌人数')),
                ('shareNumber', models.IntegerField(verbose_name='分享人数')),
            ],
            options={
                'db_table': 'Song',
            },
        ),
        migrations.CreateModel(
            name='Song_Sheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='当前歌曲在歌单的排行')),
                ('sheet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.Sheet', verbose_name='歌单外键')),
                ('song', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.Song', verbose_name='歌曲外键')),
            ],
            options={
                'db_table': 'Song_Sheet',
            },
        ),
        migrations.AddField(
            model_name='resource',
            name='song',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.Song', verbose_name='歌曲外键'),
        ),
    ]
