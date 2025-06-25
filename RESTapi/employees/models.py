from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_id = models.CharField(max_length=10, unique=True)
    name= models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    position = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.name}  {self.position}"