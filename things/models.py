from django.db import models

class Thing(models.Model):
    name = models.CharField(unique=True,blank=False,max_length=30)
    description = models.CharField(unique=False,max_length=120)
    quantity = models.PositiveIntegerField(unique=True,validators=[MinValueValidator(1), MaxValueValidator(100)])
