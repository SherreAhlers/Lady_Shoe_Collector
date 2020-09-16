from django.db import models

# Create your models here.

class Shoe(models.Model):
    name = models.CharField(max_length=100)
    shoe_type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name