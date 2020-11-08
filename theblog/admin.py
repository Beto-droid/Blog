from django.contrib import admin
from .models import Post, Categories


admin.site.register(Post)   # this will allows uour blog psot to be accesible from our admin area
admin.site.register(Categories)
