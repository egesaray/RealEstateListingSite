from django.db import models
from django.contrib.auth.models import User



class ourUser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)  # relation with django's user # will be implemented later
    username = models.CharField(max_length=255,null=True)
    first_name = models.CharField(max_length=255,null=True)
    last_name = models.CharField(max_length=255,null=True)
    email = models.EmailField(max_length=254)
    #phone number for product details
    def __str__(self):
        return self.username


city=[
    (' İstanbul/Asya',' İstanbul/Asya'),
    ('İstanbul/Avrupa','İstanbul/Avrupa'),
    ('Ankara', 'Ankara'),
    (' İzmir', ' İzmir'),
    ('Eskişehir', 'Eskişehir'),
    ('Adana', 'Adana'),
    ('Karabük', 'Karabük'),
    ('Uşak', 'Uşak'),
    ('Konya', 'Konya'),
    ('Antalya', 'Antalya'),
    ('Mersin', 'Mersin'),
    ('Diyarbakır', 'Diyarbakır'),
    ('Sakarya', 'Sakarya'),
    ('Eskişehir', 'Eskişehir'),
    ('Van', 'Van'),
    ('Kars', 'Kars'),
    ('Amasya', 'Amasya'),
    ('Balıkesir', 'Balıkesir'),
    ('Muğla', 'Muğla'),
    ('Batman', 'Batman'),
    ('Kocaeli', 'Kocaeli'),
]
RorS = [
    ('For Sale', 'For Sale'),
    ('For Rent', 'For Rent'),
]
Furniture = [
    ('Yes', 'Yes'),
    ('No', 'No'),
]
b_types = [
    ('Apartment', 'Apartment'),
    ('House', 'House'),
    ('Flat', 'Flat'),
    ('Town house', 'Town house'),
    ('Villa', 'Villa'),
    ('Others', 'Others'),
]

class Post(models.Model):
    ouruser = models.ForeignKey(ourUser, null=True, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=255,null=True)
    post_description = models.TextField()
    price = models.DecimalField(decimal_places=2 , max_digits=12)
    location = models.CharField(max_length=255,null=True,choices=city)
    postType = models.CharField(choices=RorS , max_length=50, null=True , default='For Sale')
    floor = models.DecimalField(decimal_places=0 , max_digits=3 ,null=True)
    building_age = models.DecimalField(decimal_places=0, max_digits=2 , null=True)
    area = models.DecimalField(decimal_places=0,max_digits=4 ,null=True)
    isFurniture = models.CharField(choices=Furniture ,null=True,max_length=50,default="No")
    building_type = models.CharField(choices=b_types ,null=True ,max_length=50)


    def __str__(self):
        return self.post_title


class PostImages(models.Model):
    image = models.ImageField(null=True, blank=True)
    gallery = models.ForeignKey(Post,null=True,on_delete= models.CASCADE)

