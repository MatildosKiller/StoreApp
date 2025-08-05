from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
product_cars = {"Ferrary":3000,"Bentley":5000,"Zhiguli":700000}
def index(request):
    
     
    return HttpResponse(f"""
        <p>Host: {host}</p>
        <p>Path: {path}</p>
        <p>User-agent: {user_agent}</p>
    """)
def info_car(request):
    
    name = request.GET.get("car","Undefined")
    res = product_cars.get(name,"нет такой машины")

    return HttpResponse(f"{name} - {res}")

def user(request): 
    age = request.GET.get("age", 0)
    name = request.GET.get("name", "Undefined")
    return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")

def about(request,name, age):
    return HttpResponse(f"Жил-был чувак - {name} ему - {age} годика(ов)")
 
def contact(request):
    return HttpResponse("Контакты")

def buy(request):
    return

def cars(request):
    return HttpResponse(f"список машин")

    

def top(request):

    return HttpResponse(f"top продаж машин")

def new(request):

    return HttpResponse(f"список новых машин")

