from django.db import models

# Create your models here.

class Parent(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    
    def __str__(self):
        return f'{self.name} - {self.lastname}'

class Child(models.Model):
    childname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.childname} - {self.lastname}'
    