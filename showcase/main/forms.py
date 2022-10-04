from django import forms

# class name is the name of our form
# inherits from django.forms.Form
class addExercise(forms.Form):
    exerciseName = forms.CharField(label="Exercise Name", max_length=200, required=True)
    exerciseSets = forms.CharField(label="Exercise Sets", max_length=4, required=True)
    exerciseReps = forms.IntegerField(label="Exercise Reps", required=True)
    exerciseComment = forms.CharField(label="Exercise Comment", max_length=400, required=True)