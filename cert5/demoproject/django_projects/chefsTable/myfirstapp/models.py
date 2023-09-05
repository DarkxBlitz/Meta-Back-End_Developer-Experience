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
    updated_at = models.DateTimeField(auto_now=True) 
    food_service = models.CharField(max_length = 200, choices=FOOD_SERVICE, default='Delivery')

class Reservation(models.Model):
    name = models.CharField(max_length=100, blank=True)
    contact = models.CharField('Phone number', max_length=300)
    time = models.DateTimeField(auto_now=True)
    count = models.IntegerField()
    notes = models.CharField(max_length=300,blank=True)

    def __str__(self):
        return self.name
''' I can use the str method to override the default representation of the object and define my own. I want this representation to be the name of the customer. So using the return statement, I type self.name which will display the value stored in the name attribute of the object. I save this file and then go back to the browser and refresh the web page. Notice that the name of the reservation objects have now been renamed according to the customer.'''
