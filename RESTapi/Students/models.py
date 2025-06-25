from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)
    course = models.CharField(max_length=100, default='General')  # 👈 Default added here

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Students"
        ordering = ['name']
