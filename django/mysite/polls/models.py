from django.db import models


class Series(models.Model):
    name = models.CharField(max_length=20)
    brires = models.TextField()

    def __str__(self):
        return u'%s' % self.name


class Card(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return u'%s' % self.name
