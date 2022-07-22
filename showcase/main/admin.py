from django.contrib import admin
from .models import workoutList

# Register your models here.
# Registering a model means that it will appear in the admin portal
admin.site.register(workoutList)
