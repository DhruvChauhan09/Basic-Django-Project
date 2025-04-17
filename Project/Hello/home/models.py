from django.db import models

# Create your models here.
class Login(models.Model):
    username= models.CharField(max_length=122)
    password= models.CharField(max_length=8)
    date= models.DateField()

    def __str__(self):                 ## to return user name in admin panel
        return self.username
    


class Contacts(models.Model):
    name= models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    phone= models.CharField(max_length=12)
    desc= models.TextField()
    date= models.DateField()

    def __str__(self):                 ## to return user name in admin panel
        return self.name  