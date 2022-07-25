from django.db import models

# Create your models here.
class workoutList(models.Model):
    name = models.CharField(max_length=200)
    # woDate = models.DateTimeField('Date of workout')
    def __str__(self):
        return self.name

# workoutEntry will be a part of workoutEntry
class workoutEntry(models.Model):
    # This variable identifies a foreign key to connect it to workoutEntry
    workout = models.ForeignKey(workoutList, on_delete=models.CASCADE)
    exerciseName = models.CharField(default="default", max_length=40)
    exerciseSets = models.CharField(default="0", max_length=4)
    exerciseReps = models.CharField(default="0", max_length=4)
    exerciseComment = models.CharField(max_length=400)
    # This is a boolean field to identify if the item is complete
    # complete = models.BooleanField()
    
    def __str__(self):
        return '%s %s %s %s' %(self.exerciseName, self.exerciseSets, self.exerciseReps, self.exerciseComment)