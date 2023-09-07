from django.db import models
from django.urls import reverse

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self) :
        return self.name