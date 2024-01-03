from django.db import models

# Create your models here.

class Bank(models.Model):
    isBankrupt = models.BooleanField(default=False)