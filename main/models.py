from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255, default='')
    amount = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    description = models.TextField(default='')

    def __str__(self) :
        return self.name