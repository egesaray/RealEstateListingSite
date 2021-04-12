
import django_filters
from django import forms
from .models import *


class PostFilter(django_filters.FilterSet):
    class Meta:
        model=Post
        fields = ['location','price','area','building_age','post_title']
