from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField()
    # email = models.EmailField()

class Product(models.Model):
    pass

class Cars(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.car_name