from django.db import models

# Create your models here.


from django.db import models
from django.utils import timezone

class Medication(models.Model):
    name = models.CharField(max_length=200)
    dosage = models.IntegerField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f"{self.name}"

class Schedule(models.Model):
   medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
   days_of_week = models.IntegerField()
   start_time = models.TimeField()
   end_time = models.TimeField()

   def __str__(self):
    return f"{self.medication}"


    
    #add in doctors name later