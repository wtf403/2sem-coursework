# Generated by Django 4.0.5 on 2022-06-24 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('video_type', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_type', models.CharField(max_length=64, verbose_name='Тип видео')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
            },
        ),
    ]
