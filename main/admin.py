from django.contrib import admin

from .models import *

admin.site.register(ourUser)
admin.site.register(Post)
admin.site.register(PostImages)