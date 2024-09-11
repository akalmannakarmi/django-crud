from django.db import models

# Create your models here.
class Address(models.Model):
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

class Info(models.Model):
    firstName = models.CharField(max_length=25)
    middleName = models.CharField(max_length=25,blank=True)
    lastName = models.CharField(max_length=25)
    dob = models.DateField()
    address = models.ForeignKey(Address,null=True,blank=True,on_delete=models.SET_NULL,related_name="infos")