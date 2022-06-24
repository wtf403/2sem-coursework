# Generated by Django 4.0.5 on 2022-06-24 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Имя')),
                ('surname', models.CharField(max_length=64, verbose_name='Фамилия')),
                ('born', models.DateField(verbose_name='Родился')),
                ('dies', models.DateField(verbose_name='Умер')),
                ('birthplace', models.CharField(max_length=64, verbose_name='Место рождения')),
                ('nationality', models.CharField(max_length=64, verbose_name='Нацональность')),
                ('photo_url', models.ImageField(upload_to='dierctors/cover', verbose_name='Обложка')),
                ('video', models.ManyToManyField(related_name='director', to='video.video', verbose_name='Видео')),
            ],
            options={
                'verbose_name': 'Режиcёр',
                'verbose_name_plural': 'Режиcёры',
            },
        ),
    ]