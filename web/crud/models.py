from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=40)
    lastname  = models.CharField(max_length=40)
    address   = models.CharField(max_length=50)
    gender    = models.CharField(max_length=20)
    email     = models.CharField(max_length=40)

    def __str__(self):
        return self.firstname + " " + self.lastname + " " + self.address + " " + self.gender + " " + self.email
