# Generated by Django 2.1.1 on 2018-09-30 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20180930_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='song',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.Song', verbose_name='歌曲外键'),
        ),
    ]