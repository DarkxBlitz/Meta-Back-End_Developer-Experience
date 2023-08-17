from django.db import models
from django.forms import ModelForm

FOOD_SERVICE = (
    ("Delivery", "Delivery"),
    ("Order In", "Order In"),
    ("Take out", "Take out"),
)

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length = 100)
    cuisine = models.CharField(max_length = 100)
    price = models.IntegerField()

class InputForm(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.TimeField()
    food_service = models.CharField(max_length = 200, choices=FOOD_SERVICE, default='Delivery')