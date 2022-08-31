from ast import If
from django.shortcuts import render,redirect
from django.urls import reverse

from cars.models import Car
# Create your views here.
def list(request):
    car_list = Car.objects.all()
    context_data = {'car_list':car_list}
    return render(request, "list.html", context = context_data)

def add(request):
    if request.POST:
        year = request.POST['year']
        brand = request.POST['brand']
        Car.objects.create(brand = brand, year = year)
        return redirect(reverse('cars:list'))
    else:
        return render (request, "add.html")

def dele(request):
    if request.POST:
        pk = request.POST['pk']
        Car.objects.get(pk=pk).delete()
        return redirect(reverse('cars:list'))
    else:
        print('wrong entry pls check again')    
        return render (request, "del.html")