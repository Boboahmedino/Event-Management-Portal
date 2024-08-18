from django.db import models

# Create your models here.

# class Payment(models.Model):
#     pay = models.CharField(max_length=300)


class Payment(models.Model):
    name = models.CharField(max_length = 300)
    
    def __str__(self):
        return self.name