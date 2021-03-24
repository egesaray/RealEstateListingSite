from django.db import models
from django.contrib.auth.models import User



class ourUser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)  # relation with django's user # will be implemented later
    username = models.CharField(max_length=255,null=True)
    first_name = models.CharField(max_length=255,null=True)
    last_name = models.CharField(max_length=255,null=True)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField(max_length=10)

    def __str__(self):
        return self.first_name + " " + self.last_name



class Post(models.Model):
    ouruser = models.ForeignKey(ourUser, null=True, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=255,null=True)
    post_description = models.TextField()
    price = models.DecimalField(decimal_places=2 , max_digits=12)
    location = models.CharField(max_length=255,null=True)
    RorS = [
        ('For Sale', 'For Sale'),
        ('For Rent', 'For Rent'),
    ]
    postType = models.CharField(choices=RorS , max_length=50, null=True , default='For Sale')
    floor = models.DecimalField(decimal_places=0 , max_digits=3 ,null=True)
    building_age = models.DecimalField(decimal_places=0, max_digits=2 , null=True)
    area = models.DecimalField(decimal_places=0,max_digits=4 ,null=True)
    isFurniture = models.BooleanField(default=False, null=False)
    b_types =[
        ('Apartment', 'Apartment'),
    ('House', 'House'),
    ('Flat', 'Flat'),
    ('Town house', 'Town house'),
    ('Villa', 'Villa'),
    ('Others', 'Others'),
    ]
    building_type = models.CharField(choices=b_types ,null=True ,max_length=50)


    def __str__(self):
        return self.post_title


class PostImages(models.Model):
    image = models.ImageField(null=True, blank=True)
    gallery = models.ForeignKey(Post,null=True,on_delete= models.CASCADE)

