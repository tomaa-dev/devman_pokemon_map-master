from django.db import models
from datetime import datetime


class Pokemon(models.Model):
    title = models.CharField(
        max_length=200, 
        verbose_name='Имя покемона'
    )
    photo = models.ImageField(
        upload_to="pokemon", 
        blank=True, 
        verbose_name='Фото покемона'
    )
    title_en = models.CharField(
        max_length=200, 
        blank=True, 
        verbose_name='Имя покемона (английский)'
    )
    title_jp = models.CharField(
        max_length=200, 
        blank=True, 
        verbose_name='Имя покемона (японский)'
    )
    description = models.TextField(
        blank=True, 
        verbose_name='Описание'
    )
    previous_evolution = models.ForeignKey(
        'self',
        verbose_name='Из кого эволюционирует',
        null=True,
        blank=True,
        related_name='next_evolution',
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        verbose_name='Покемон',
        on_delete=models.CASCADE
    )
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(
        blank=True, 
        verbose_name='Появился'
    )
    disappeared_at = models.DateTimeField(
        blank=True, 
        verbose_name='Исчез'
    )
    level = models.IntegerField(
        null=True, 
        blank=True,
        verbose_name='Уровень'
    )
    health = models.IntegerField(
        null=True, 
        blank=True,
        verbose_name='Здоровье'
    )
    strength = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Сила'
    )
    defence = models.IntegerField(
        null=True, 
        blank=True,
        verbose_name='Защита'
    )
    stamina = models.IntegerField(
        null=True, 
        blank=True,
        verbose_name='Выносливость'
    )

    def __str__(self):
        text = (
            f'Координаты покемона {self.pokemon.title} - {self.lat} {self.lon}'
        )
        return text