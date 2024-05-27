import uuid
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import Signal,receiver


# Create your models here.

class Profil(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    info = models.CharField(max_length=100,null=True,blank=True)
    location = models.CharField(max_length=150,null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    social_git_hub = models.CharField(max_length=150,null=True,blank=True)
    social_facebook = models.CharField(max_length=150,null=True,blank=True)
    social_youtube = models.CharField(max_length=150,null=True,blank=True)
    social_instagram = models.CharField(max_length=150,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='profiles',default='images/user.png')
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)


    def __str__(self):
        return str(self.user.username)


class Skill(models.Model):
    user = models.ForeignKey(Profil,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return str(self.name)


