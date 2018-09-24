from django.db import models


class Series(models.Model):
    name = models.CharField(max_length=20)
    brires = models.TextField()


class Card(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
