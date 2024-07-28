from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.IntegerField()
    address=models.CharField(max_length=100,default=False)
    designation=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    manager=models.CharField(max_length=100)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    