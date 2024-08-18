from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.
class Profile(models.Model):
    customer = models.ForeignKey(User, on_delete= models.CASCADE)
    mobile_number = models.CharField(max_length=20)
    address = models.CharField(max_length= 300)
    country = models.CharField(max_length = 300)
    state = models.CharField(max_length= 300)
    
    def __str__(self):
        return self.customer.username
    
    class Meta:
        verbose_name_plural = 'Profiles'
    
    
class Reservation(models.Model):
    customer = models.ForeignKey(User, on_delete= models.CASCADE)
    # profile = models.ForeignKey(Profile, on_delete= models.CASCADE)
    event_title = models.CharField(max_length= 300)
    category = models.CharField(max_length=300)
    start_date = models.DateField(default = now)
    end_date = models.DateField(default = now)
    guest = models.IntegerField()
    time = models.TimeField( auto_now=False, auto_now_add=False)  
    room = models.CharField(max_length=300)
    breakout = models.CharField(max_length=300)
    catering = models.CharField(max_length=300)
    venue = models.CharField(max_length=300)
    confirmation = models.CharField(max_length = 10)
    datetime = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return "Reservation by " + str(self.customer.username) + " on the " + str(self.datetime)[:19]

    class Meta:
        
        ordering = ['-start_date'] 
        
    class Meta:
        ordering = ['-end_date'] 
        
            
class Category(models.Model):
    name = models.CharField(max_length=300)
    
    class Meta:
        verbose_name_plural = '_Categories'
        
    def __str__(self):
        return self.name
        
        
class Room(models.Model):
    name = models.CharField(max_length = 300)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = '_Room'


class Breakout(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = '_Breakout'
    
class Catering(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = '_Catering'
    
class Venue(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = '_Venues'
