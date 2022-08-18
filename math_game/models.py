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

class Math_score(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        default=NULL,
        related_name='players'
    )
    operator = models.CharField(max_length=50)
    max_range = models.SmallIntegerField(default=2)
    score = models.IntegerField(default=0)
    point = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
       ordering = ["-point"]
       paginate_by: 5

    def createdDate(self):
        self.created = timezone.now()
        self.save()

    def __str__(self):
        return self.operator

class Addition_score(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT, 
        blank= True, 
        null=True,
        related_name='additionPlayer'
    )
    operator = models.CharField(max_length=50)
    max_range = models.SmallIntegerField(default=2)
    score = models.IntegerField(default=0)
    point = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )


    def get_absolute_url(self):
        return reverse('math_game:addition', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)

    class Meta:
       ordering = ["-point"]
       paginate_by: 5
       
    def __str__(self):
        return self.operator
class Division_score(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT,
        blank= True, 
        null=True,
        related_name='divisionScore'
    )
    operator = models.CharField(max_length=50)
    max_range = models.SmallIntegerField(default=2)
    score = models.IntegerField(default=0)
    point = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )


    def get_absolute_url(self):
        return reverse('math_game:division', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)

    class Meta:
       ordering = ["-point"]
       
    def __str__(self):
        return self.operator
class Multiplication_score(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT,
        blank= True, 
        null=True,
        related_name='multiplicationScore'
    )
    operator = models.CharField(max_length=50)
    max_range = models.SmallIntegerField(default=2)
    score = models.IntegerField(default=0)
    point = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )


    def get_absolute_url(self):
        return reverse('math_game:multiplication', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)

    class Meta:
       ordering = ["-point"]
       
    def __str__(self):
        return self.operator
class Subtraction_score(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT,
        blank= True, 
        null=True,
        related_name='subtractionScore'
    )
    operator = models.CharField(max_length=50)
    max_range = models.SmallIntegerField(default=2)
    score = models.IntegerField(default=0)
    point = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )


    def get_absolute_url(self):
        return reverse('math_game:subtraction', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)

    class Meta:
       ordering = ["-point"]
       
    def __str__(self):
        return self.operator

class Comment_math(models.Model):
    GAME_TYPES = (
        (None, '--Please choose--'),
        ('Ad', 'Addition'),
        ('Div', 'Division'),
        ('Mul', 'Multiplication'),
        ('Sub', 'Subtraction'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        default=NULL,
        related_name='player_comment'
    )
    game_type = models.CharField(max_length=10, choices=GAME_TYPES)
    comment = models.TextField(max_length=300)
    active =  models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def get_absolute_url(self):
        return reverse('my-comment')

    def __str__(self):
        return 'Comment_math {} by {}'.format(self.user ,self.game_type ,self.comment,self.created)
