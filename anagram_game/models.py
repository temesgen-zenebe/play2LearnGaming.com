from asyncio.windows_events import NULL
from django.db import models
from django.conf import settings
from django.utils.timezone import datetime
from common.utils.text import unique_slug
from django.urls import reverse
from django.utils import timezone
from ast import Mod
from zipapp import create_archive


class Anagram_score(models.Model):
  
    users = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.PROTECT,
            default=NULL,
            related_name='anagramPlayer'
    )
    word_size = models.CharField(max_length=10)
    score = models.IntegerField(default=0)
    point = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, unique=True, null=False, editable=False,)

    class Meta:
       ordering = ["-point"]
       paginate_by: 5

    def get_absolute_url(self):
        return reverse('anagram_game:score', args=[self.slug])

    def createdDate(self):
        self.created = timezone.now()
        self.save()

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.word_size
    
class Comment_Anagram(models.Model):
    GAME_TYPES = ((None, '--Please choose--'), ('anagrame', 'AnagrameHunt'),)
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        default=NULL,
        related_name='comment_anagrame',
    )
    game_type = models.CharField(max_length=10, choices=GAME_TYPES)
    comment = models.TextField(max_length=300)
    active =  models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def get_absolute_url(self):
        return reverse('comment_anagrame')

    def __str__(self):
        return 'Games_comment {} by {}'.format(self.user,self.game_type,self.comment,self.active,self.created)