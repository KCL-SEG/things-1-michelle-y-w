from django.db import models
from django.db.models.Model import models

class Thing(models.Model):
    name = models.CharField()
    description = models.TextField()
    quantity = models.integerField()
    
