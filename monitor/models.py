from django.db import models

# Create your models here.
class IOT(models.Model):
    device_id = models.AutoField(primary_key='true')
    device_name = models.CharField(max_length=255, default=None)
    device_current = models.DecimalField(max_digits=5, max_length=5, decimal_places=2)
    device_voltage = models.DecimalField(max_digits=5, max_length=5, decimal_places=2)
    device_kw = models.DecimalField(max_digits=5, max_length=5, decimal_places=2)
    hours = models.PositiveIntegerField()

class Login(models.Model):
	username=models.CharField(max_length=20,primary_key=True)
	password=models.CharField(max_length=10)
