from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=10)
    stock = models.IntegerField(max_length=30)
    price = models.FloatField(max_length=100)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name
