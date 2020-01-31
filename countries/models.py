from django.db import models
from django.utils.translation import gettext_lazy as _


class CountriesAsia(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(region='1')

class CountriesEurope(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(region='2')

class CountriesAfrica(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(region='3')

class CountriesOceania(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(region='4')

class CountriesAmerica(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(region='5')

class CountriesOther(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(region='6')

class Country(models.Model):
    """Country model."""
    
    iso_code = models.CharField(max_length=2,unique=True)
    name = models.CharField(max_length=255,unique=True)
    region = models.CharField(max_length=1, null=True, choices=[
        ('1', _('Asia')), 
        ('2', _('Europe')),
        ('3', _('Africa')),
        ('4', _('Oceania')),
        ('5', _('America')),
        ('6', _('Antartica'))
    ])

    objects = models.Manager()
    asia_objects = CountriesAsia()
    europe_objects = CountriesEurope()
    africa_objects = CountriesAfrica()
    america_objects = CountriesAmerica()
    oceania_objects = CountriesOceania()
    others_objects = CountriesOther()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name