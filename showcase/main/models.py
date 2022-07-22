from django.db import models

# Create your models here.
class workoutList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# workoutEntry will be a part of workoutEntry
class workoutEntry(models.Model):
    # This variable identifies a foreign key to connect it to workoutEntry
    workout = models.ForeignKey(workoutList, on_delete=models.CASCADE)
    workoutReps = models.CharField(max_length=2)
    workoutComment = models.CharField(max_length=400)
    # This is a boolean field to identify if the item is complete
    # complete = models.BooleanField()
    
    def __str__(self):
        return self.workoutReps, self.workoutComment