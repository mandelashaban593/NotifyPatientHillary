
from django.db import models
from django.utils import timezone
   
  #Create Medication model 

class Medication(models.Model):
    name = models.CharField(max_length=200)
    
    
    
    def __str__(self):
        return f"{self.name}"

 #Create Schedule model

class Schedule(models.Model):
   medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
   dosage = models.IntegerField(default=0)
   days_of_week = models.IntegerField()
   start_date = models.DateField(default=timezone.now)
   start_time = models.TimeField()
   end_date = models.DateField(default=timezone.now)
   end_time = models.TimeField()
   
   
   
   
   def __str__(self):
    return f"{self.medication}: dosage={self.dosage}, days_of_week={self.days_of_week}, start_date={self.start_date}, start_time={self.start_time}, end_date={self.end_date}, end_time={self.end_time}"

 #Create notification function to generate notification message

   def generate_notification_message(self):
    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    day = days_of_week[self.days_of_week]
    start_time = self.start_time.strftime('%I:%M %p')
    end_time = self.end_time.strftime('%I:%M %p')
    return f"Take {self.medication.name} {self.dosage}mg every {day} from {start_time} to {end_time}"


 #Create function to print  notification message to the console

   def output_notification(self):
        current_time = timezone.localtime(timezone.now()).time()
        if self.start_time <= current_time <= self.end_time:
            notification = self.generate_notification_message()
            print(notification)

    
    #add in doctors name later