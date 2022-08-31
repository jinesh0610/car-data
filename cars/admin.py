from django.contrib import admin
from cars.models import Car

# Register your models here.
class Caradmin(admin.ModelAdmin):
    pass
   
admin.site.register(Car, Caradmin)