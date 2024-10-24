from django.db import models
from django.core.validators import MaxLengthValidator


class ConcatUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone =  models.CharField(max_length=11)
    body = models.TextField()

    def __str__(self):
        return self.name