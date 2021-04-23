from django.db import models

# Create your models here.

class Patient(models.Model):
    lastName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    contact = models.IntegerField()
    barangay = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    houseNo = models.IntegerField()
    city = models.CharField(max_length=100)
    age = models.IntegerField()
    dateOfBirth = models.CharField(max_length=100)
    vaccineName = models.CharField(max_length=100)
    image = models.ImageField(upload_to='directory/images')

    def __str__(self):
        return self.lastName