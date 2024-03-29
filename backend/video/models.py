from tkinter import CASCADE
from xml.etree.ElementTree import Comment
from django.db import models
from studio.models import Studio
from genre.models import Genre
from director.models import Director
from actor.models import Actor
from video_type.models import VideoType

# Create your models here.
class Video(models.Model):
    image_url = models.CharField(verbose_name='Ссылка на обложку', max_length=255, blank=True)
    image_url_x2 = models.CharField(verbose_name='Ссылка на обложку (Retina)', max_length=255, blank=True)
    video_url = models.CharField(verbose_name='Ссылка на трейлер', max_length=255, blank=True)
    
    title = models.CharField(verbose_name='Название', max_length=255)
    v_type = models.ForeignKey(VideoType, on_delete=models.PROTECT, verbose_name='Тип видео', related_name='v_type') 
    description = models.TextField(verbose_name='Описание')

    director = models.ManyToManyField(verbose_name='Режисёры', to=Director, related_name='video')
    actor = models.ManyToManyField(verbose_name='Актёры', to=Actor, related_name='video')
    
    duration = models.TimeField(verbose_name='Продолжительнось')
    release = models.DateField(verbose_name='Дата выхода')
    country = models.CharField(verbose_name='Старна', max_length=64)
    age_restriction	= models.IntegerField(verbose_name='Возрастное ограничение')
    budget = models.CharField(verbose_name='Бюджет', max_length=64)
    fees = models.CharField(verbose_name='Сборы', max_length=64)
    
    studio = models.ManyToManyField(verbose_name='Стyдии', to=Studio, related_name='video')
    genre = models.ManyToManyField(verbose_name='Жанры', to=Genre, related_name='video')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
