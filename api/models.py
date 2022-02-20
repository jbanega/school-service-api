from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    grade = models.CharField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'