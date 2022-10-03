from django.shortcuts import render
from django.core.exceptions import MultipleObjectsReturned
from django.http import HttpResponse, HttpResponseRedirect
from .models import workoutList, workoutEntry
from .forms import addExercise

# Create your views here.

def index(response):
    return render(response, "main/home.html")

def workout(response):
    try:
        w = workoutList.objects.get()
    except MultipleObjectsReturned:
        w = workoutList.objects.filter().first()
    return render(response, "main/workout.html",{"w":w})

# Form to add a new workout
def addWorkout(response):
    if response.method == "POST":
        form = addExercise(response.POST)

        if form.is_valid():
            n = form.cleaned_data["exerciseName"]
            wo = workoutList(name = n)
            wo.save()

        return HttpResponseRedirect("/workout/")
        #return HttpResponseRedirect("/%i" %wo.id)
    else:
        form = addExercise()
    return render(response, "main/addWorkout.html", {"form":form})