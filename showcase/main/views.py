from django.shortcuts import render
from django.http import HttpResponse
from .models import workoutList, workoutEntry

# Create your views here.

def index(response):
    return render(response, "main/home.html")

def workout(response):
    w = workoutList.objects.get()
    return render(response, "main/workout.html",{"w":w})