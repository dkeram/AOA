from django.db import models

# Create your models here.
class Phones(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number_1 = models.IntegerField(max_length=9)
    phone_number_2 = models.IntegerField(max_length=9)
    email = models.EmailField()