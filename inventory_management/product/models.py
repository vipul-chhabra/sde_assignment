from django.db import models

# Create your models here.


class Product(models.Model):
    name: str = models.CharField(max_length=200)
    price: str = models.FloatField()
    category: float = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

