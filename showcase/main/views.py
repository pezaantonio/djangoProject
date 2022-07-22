from django.shortcuts import render
from django.http import HttpResponse
from .models import workoutList, workoutEntry

# Create your views here.

def index(response):
    return HttpResponse("Hello world")
