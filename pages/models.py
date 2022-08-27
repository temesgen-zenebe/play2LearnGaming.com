from ast import Mod
from asyncio.windows_events import NULL
from zipapp import create_archive
from django.db import models
from django.conf import settings
from django.utils.timezone import datetime
from common.utils.text import unique_slug
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Games_comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        default=NULL,
        related_name='game_comment'
    )
    email = models.EmailField(max_length = 254)
    comment = models.TextField(max_length=300)
    active =  models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True )

    class Meta:
        ordering = ['created']

    def get_absolute_url(self):
        return reverse('game-comment')

    def __str__(self):
        return 'Games_comment {} by {}'.format(self.user,self.comment,self.active,self.created)
    
class SubscribedUsers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self):
        return self.email  
    
      
class SiteVisitersCounter(models.Model):
    visits_num = models.IntegerField(default=1)
    updated_date = models.DateTimeField('Date updated', default=timezone.now)
    
    def __str__(self):
        return  str(self.visits_num )
    
class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=500 )
    created_date = models.DateTimeField('created', default=timezone.now)

    def __str__(self):
        return self.email