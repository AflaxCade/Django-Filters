from django.db import models

# Create your models here.

class Person(models.Model):

    sex_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=100, choices=sex_choices)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
