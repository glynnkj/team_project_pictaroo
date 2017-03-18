from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
#Create two classes - one class representing each model.
#Both must inherit from the Model base class,
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self): #For Python 2, use _unicode_ too
        return self.name


class UserProfile(models.Model):
#This line is required. Links UserProfile to a User Model Instance
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    bio = models.TextField(default='', blank=True)

    #Override the __unicode__() method to return out something meaningful

    def __str__(self):
        return self.user.username

class Image(models.Model):
    category = models.ForeignKey(Category)

    title = models.CharField(max_length=128)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    category = models.ForeignKey(Category)
    author = models.ForeignKey(UserProfile)
    title = models.CharField(max_length=128)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    date = models.DateTimeField(default=timezone.now(), unique=True)
    image = models.ForeignKey(Image)
    author = models.ForeignKey(UserProfile)

    text = models.TextField(default='', blank=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.text

