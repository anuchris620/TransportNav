from django.db import models

# Create your models here.
class Stops_time(models.Model):
    Routes=models.CharField(max_length=200)
    Route_time=models.CharField(max_length=200,blank=True)
    time1=models.CharField(max_length=200)
    time2=models.CharField(max_length=200)
    time3=models.CharField(max_length=200)
    time4=models.CharField(max_length=200)
    time5=models.CharField(max_length=200,blank=True)
    time6=models.CharField(max_length=200,blank=True)
    time7=models.CharField(max_length=200,blank=True)
    time8=models.CharField(max_length=200,blank=True)
    time9=models.CharField(max_length=200,blank=True)
    time10=models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.Routes
    
class CET_PATTOM_EASTFORT(models.Model):
    Route=models.CharField(max_length=200)
    Stop1=models.CharField(max_length=200)
    Stop2=models.CharField(max_length=200)
    Stop3=models.CharField(max_length=200)
    Stop4=models.CharField(max_length=200)
    Stop5=models.CharField(max_length=200)
    Stop6=models.CharField(max_length=200)
    Stop7=models.CharField(max_length=200)
    Stop8=models.CharField(max_length=200)
    Stop9=models.CharField(max_length=200)
    def __str__(self):
        return self.Route
    
class Stops(models.Model):
    Route=models.CharField(max_length=200)
    Stop1=models.CharField(max_length=200)
    Stop2=models.CharField(max_length=200)
    Stop3=models.CharField(max_length=200)
    Stop4=models.CharField(max_length=200)
    Stop5=models.CharField(max_length=200)
    Stop6=models.CharField(max_length=200)
    Stop7=models.CharField(max_length=200)
    Stop8=models.CharField(max_length=200)
    Stop9=models.CharField(max_length=200)
    Stop10=models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.Route
