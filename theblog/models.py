from django.db import models
from django.contrib.auth.models import User   # importing User created in the admin page (superuser)
from django.urls import reverse
from datetime import date, datetime


class Categories(models.Model):
    name = models.CharField(max_length=255)  #  admin section ?

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #  return reverse('article-detail', args=(str(self.id)))
        #  return reverse('article-detail', args=(str(self.pk)))
        #  return reverse('home', kwargs={'pk': self.pk})
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)   #  author, its the user , on_delete it deletes all the post when the user its removed
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='coding')

    def __str__(self):
        return self.title + ' | ' + str(self.author)   #  allows us on our admin page to see the title of the blog psot and the author instead a string of weird numbers

    def get_absolute_url(self):
        #  return reverse('article-detail', args=(str(self.id)))
        #  return reverse('article-detail', args=(str(self.pk)))
        return reverse('article-detail', kwargs={'pk': self.pk})

