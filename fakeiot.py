from django.shortcuts import render,redirect
from monitor.models import *
from monitor.models import IOT
from django.http import *
from django.contrib import messages
from faker import Faker
import numpy as np
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "monitor.settings")
import django
django.setup()


fake = Faker()
Faker.seed(313)
for i in range(10):
    device_name = fake.name()
    device_current= fake.number()
    device_voltage= fake.number()
    device_kw= fake.number()
    hours= fake.number()
    iotinfo =IOT(device_name=fake.name,device_current=fake.number,device_voltage=fake.number,device_kw=fake.number,hours=fake.number)
    iotinfo.save()
print(device_name)
