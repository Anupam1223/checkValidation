from django.db import models

# Create your models here.
class CustomUser(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
