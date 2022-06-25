# Generated by Django 4.0.5 on 2022-06-24 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video_type', '0002_initial'),
        ('video', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='image_url_x2',
            field=models.CharField(blank=True, max_length=255, verbose_name='Ссылка на обложку (Retina)'),
        ),
        migrations.AlterField(
            model_name='video',
            name='v_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='v_type', to='video_type.videotype', verbose_name='Тип видео'),
        ),
    ]