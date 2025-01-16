from django.db import models

# Create your models here.
class Buyer(models.Model):
    name =models.CharField
    balance = models.DecimalField
    age = models.IntegerField

class Game(models.Model):
    title = models.CharField
    cost = models.DecimalField
    size = models.DecimalField
    description = models.TextField
    age_limited = models.BooleanField
    buyer = models.ManyToManyField(Buyer, related_name="games")
