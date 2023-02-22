from django.db import models

# Create your models here.
class pics(models.Model):
    img = models.ImageField(upload_to='image')
    id = models.CharField(max_length=10,primary_key=True)
    name=models.CharField(max_length=100)

class Profile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    fullname = models.CharField(max_length=100)
    password= models.CharField(max_length=50)

    def create(cls,fullname,username,email,password):
        profile=cls(fullname=fullname,username=username,email=email,password=password)

        return profile