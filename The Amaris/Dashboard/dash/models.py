from datetime import datetime

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Cus_Res(models.Model):
    Cus_id = models.AutoField
    Cus_name = models.CharField(max_length=50)
    Checkin = models.DateField(default=datetime.now())
    Checkout = models.DateField(default=datetime.now())
    Easeofonlinebooking = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)], default=0)
    wifi_Service = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)], default=0)
    FoodDrinks = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)], default=0)
    DepartureArrivalConvinience = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)], default=0)
    Checkinoutservice = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)], default=0)
    Cleanliness = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)], default=0)
    OtherServices = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)], default=0)
    Satisfication = models.CharField(max_length=20)

    def __str__(self):
        return self.Cus_name