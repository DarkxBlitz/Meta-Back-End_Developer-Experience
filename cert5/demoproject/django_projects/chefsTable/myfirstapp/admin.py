from django.contrib import admin

from .models import InputForm
from .models import Reservation
# Register your models here.
admin.site.register(InputForm)
admin.site.register(Reservation)