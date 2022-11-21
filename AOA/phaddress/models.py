from django.db import models

# Create your models here.
class Phones(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number_1 = models.IntegerField()
    phone_number_2 = models.IntegerField()
    email = models.EmailField()