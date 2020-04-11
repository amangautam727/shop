from django.db import models

# Create your models here.

class shoping(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 50)
    desc = models.TextField()
    price = models.FloatField(max_length=4)
    discount = models.IntegerField()
    category =models.CharField(max_length=15)
    image_link =models.CharField(max_length=150)
    created_at=models.DateField()