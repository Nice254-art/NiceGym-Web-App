from django.db import models

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.firstname+" "+self.lastname


class Booking(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField(0)
    phone = models.IntegerField(max_length=15)
    classes = models.CharField(max_length=50,default="Aerobics")


    def __str__(self):
        return self.name