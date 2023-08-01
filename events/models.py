from django.db import models

# Create your models here.
class Meeting(models.Model):
    name = models.CharField(max_length=125)
    date_time = models.DateTimeField() # combine date & time so can do a time to meeting calc
    location = models.CharField(max_length=125) # make this a relationship and save locations 
    details = models.TextField()  
    requirements = models.CharField(max_length=250)
    reminder = models.DateTimeField()
    created = models.DateField(auto_now_add=True) # Will do a datetime.date.now() only 1 time when the row is created
    updated = models.DateField(auto_now=True) # Will do a datetime.date.now() every time a row is updated

