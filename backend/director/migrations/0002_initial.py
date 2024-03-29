# Generated by Django 4.0.5 on 2022-06-24 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('director', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Имя')),
                ('surname', models.CharField(max_length=64, verbose_name='Фамилия')),
                ('born', models.DateField(blank=True, verbose_name='Родился')),
                ('dies', models.DateField(blank=True, verbose_name='Умер')),
                ('birthplace', models.CharField(blank=True, max_length=64, verbose_name='Место рождения')),
                ('nationality', models.CharField(blank=True, max_length=64, verbose_name='Нацональность')),
                ('photo_url', models.ImageField(blank=True, upload_to='dierctors/cover', verbose_name='Обложка')),
            ],
            options={
                'verbose_name': 'Режиcёр',
                'verbose_name_plural': 'Режиcёры',
            },
        ),
    ]
