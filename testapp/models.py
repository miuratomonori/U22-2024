from django.db import models

# Create your models here.
class Day(models.Model):
    year = models.DateField('年月日',max_length=255)
    average = models.FloatField('平均気温')
    max = models.FloatField('最高気温')
    min = models.FloatField('最低気温')

class Month(models.Model):
    year = models.IntegerField('年')
    month = models.IntegerField('月')
    average = models.FloatField('平均気温')
    max_average = models.FloatField('最高平均気温')
    min_average = models.FloatField('最低平均気温')
    max = models.FloatField('最高気温')
    min = models.FloatField('最低気温')

class Year():
    year = models.IntegerField('年')
    average = models.FloatField('平均気温')
    max_average = models.FloatField('最高平均気温')
    min_average = models.FloatField('最低平均気温')
    max = models.FloatField('最高気温')
    min = models.FloatField('最低気温')