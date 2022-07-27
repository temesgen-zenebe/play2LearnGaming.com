from django.db import models
from django.conf import settings
from django.utils.timezone import datetime
# Create your models here.


class Anagram_score(models.Model):
    users = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.PROTECT,
            blank= True, 
            null=True,
            related_name='anagramPlayer'
    )
    word_size = models.SmallIntegerField(default=3)
    score = models.IntegerField(default=0)
    point = models.IntegerField(default=0)
    ranked = models.SmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word_size
        