from audioop import add
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import workoutList, workoutEntry
from .forms import addExercise

# Create your views here.

def index(response):
    return render(response, "main/home.html")

def workout(response):
    w = workoutList.objects.get()
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