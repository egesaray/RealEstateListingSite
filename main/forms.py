from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *
from django import forms



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' ,'first_name' , 'last_name' , 'email' ,'password1' , 'password2' ]



class CreatePost(ModelForm):
    class Meta:
        model = Post
        fields = ['postType' , 'isFurniture' , 'building_type' , 'location' , 'post_title' ,'price' , 'building_age','floor','post_description','area', 'room' ]


class ImagePost(ModelForm):
    class Meta:
        model= PostImages
        fields = ['image']


class OurUserForm(ModelForm):
    class Meta:
        model= User
        fields = ['username' ,'first_name' , 'last_name' , 'email']


