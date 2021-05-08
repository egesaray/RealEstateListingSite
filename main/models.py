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
    ('İstanbulAsya', 'İstanbulAsya'),
    ('İstanbulAvrupa', 'İstanbulAvrupa'),
    ('Adana', 'Adana'),
    ('Adıyaman', 'Adıyaman'),
    ('Afyonkarahisar', 'Afyonkarahisar'),
    ('Ağrı', 'Ağrı'),
    ('Amasya', 'Amasya'),
    ('Ankara', 'Ankara'),
    ('Antalya', 'Antalya'),
    ('Artvin', 'Artvin'),
    ('Aydın', 'Aydın'),
    ('Balıkesir', 'Balıkesir'),
    ('Bilecik', 'Bilecik'),
    ('Bingöl', 'Bingöl'),
    ('Bitlis', 'Bitlis'),
    ('Bolu', 'Bolu'),
    ('Burdur', 'Burdur'),
    ('Bursa', 'Bursa'),
    ('Çanakkale', 'Çanakkale'),
    ('Çankırı', 'Çankırı'),
    ('Çorum', 'Çorum'),
    ('Denizli', 'Denizli'),
    ('Diyarbakır', 'Diyarbakır'),
    ('Edirne', 'Edirne'),
    ('Elazığ', 'Elazığ'),
    ('Erzincan', 'Erzincan'),
    ('Erzurum', 'Erzurum'),
    ('Eskişehir', 'Eskişehir'),
    ('Gaziantep', 'Gaziantep'),
    ('Giresun', 'Giresun'),
    ('Gümüşhane', 'Gümüşhane'),
    ('Hakkari', 'Hakkari'),
    ('Hatay', 'Hatay'),
    ('Isparta', 'Isparta'),
    ('Mersin', 'Mersin'),
    ('İzmir', 'İzmir'),
    ('Kars', 'Kars'),
    ('Kastamonu', 'Kastamonu'),
    ('Kayseri', 'Kayseri'),
    ('Kırklareli', 'Kırklareli'),
    ('Kırşehir', 'Kırşehir'),
    ('Kocaeli', 'Kocaeli'),
    ('Konya', 'Konya'),
    ('Kütahya', 'Kütahya'),
    ('Malatya', 'Malatya'),
    ('Manisa', 'Manisa'),
    ('Kahramanmaraş', 'Kahramanmaraş'),
    ('Mardin', 'Mardin'),
    ('Muğla', 'Muğla'),
    ('Muş', 'Muş'),
    ('Nevşehir', 'Nevşehir'),
    ('Niğde', 'Niğde'),
    ('Ordu', 'Ordu'),
    ('Rize', 'Rize'),
    ('Sakarya', 'Sakarya'),
    ('Samsun', 'Samsun'),
    ('Siirt', 'Siirt'),
    ('Sinop', 'Sinop'),
    ('Sivas', 'Sivas'),
    ('Tekirdağ', 'Tekirdağ'),
    ('Tokat', 'Tokat'),
    ('Trabzon', 'Trabzon'),
    ('Tunceli', 'Tunceli'),
    ('Şanlıurfa', 'Şanlıurfa'),
    ('Uşak', 'Uşak'),
    ('Van', 'Van'),
    ('Yozgat', 'Yozgat'),
    ('Zonguldak', 'Zonguldak'),
    ('Aksaray', 'Aksaray'),
    ('Bayburt', 'Bayburt'),
    ('Karaman', 'Karaman'),
    ('Kırıkkale', 'Kırıkkale'),
    ('Batman', 'Batman'),
    ('Şırnak', 'Şırnak'),
    ('Bartın', 'Bartın'),
    ('Ardahan', 'Ardahan'),
    ('Iğdır', 'Iğdır'),
    ('Yalova', 'Yalova'),
    ('Karabük', 'Karabük'),
    ('Kilis', 'Kilis'),
    ('Osmaniye', 'Osmaniye'),
    ('Düzce', 'Düzce'),
    ('KuzeyKıbrıs', 'KuzeyKıbrıs'),
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
    room = models.DecimalField(decimal_places=0 , max_digits=3 ,null=True)




    def __str__(self):
        return self.post_title


class PostImages(models.Model):
    image = models.ImageField(null=True, blank=True)
    gallery = models.ForeignKey(Post,null=True,on_delete= models.CASCADE)


