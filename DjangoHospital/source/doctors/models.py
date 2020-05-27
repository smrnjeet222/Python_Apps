from django.db import models

# Create your models here.
class Doctor(models.Model):
    fname = models.CharField(max_length = 120)
    lname = models.CharField(max_length = 80)
    bio = models.TextField(blank=True, null=True)
    salary = models.DecimalField(default = 0 , decimal_places=2, max_digits=10000000)
    title = models.TextField(default="Dentist")
    active = models.BooleanField(default = False)