from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.

# This is for the category of booking
class Booking(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 50)
    mobile_number = models.CharField(max_length = 50)
    contact_address = models.TextField()
    # owner =models.ForeignKey(to = Customer, on_delete=models.CASCADE)
    # user =models.ForeignKey( to = Customer, on_delete=models.SET_NULL, null = True)
    event_title = models.CharField(max_length=300)
    category = models.CharField(max_length=300)
    start_date = models.DateField(default = now)
    end_date = models.DateField(default = now)
    guest = models.FloatField()
    time = models.TimeField( auto_now=False, auto_now_add=False)    
    room = models.CharField(max_length=300)
    breakout = models.CharField(max_length=300)
    catering = models.CharField(max_length=300)
    venue = models.CharField(max_length=300)
    confirmation = models.CharField(max_length = 3)

    
    
    
    def __str__ (self):
        return f'Customer: {self.last_name} {self.first_name}'

    class Meta:
        ordering = ['-start_date'] 
        
    class Meta:
        ordering = ['-end_date'] 
        
        

    
        
# This for payment modules or option

    
    
    
class Category(models.Model):
    name = models.CharField(max_length=300)
    
    class Meta:
        verbose_name_plural = 'Categories'
         #i used verbose above to change the wrong spelling of categorys in the Admin site   

    def __str__(self):
        return self.name
        
        
class Room(models.Model):
    name = models.CharField(max_length = 300)
    
    def __str__(self):
        return self.name


class Breakout(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
    
class Catering(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
    
    
class Venue(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name



