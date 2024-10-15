from django.db import models

# Create your models here.
class Items(models.Model):
    items = models.CharField(max_length=50)

    def __str__(self):
        return self.items


class Size(models.Model):
    size = models.CharField(max_length=20)

    def __str__(self):
        return self.size


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    email = models.EmailField()
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    def __str__(self):
        return self.name