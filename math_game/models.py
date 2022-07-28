from django.db import models
from django.conf import settings
from django.utils.timezone import datetime
from common.utils.text import unique_slug
from django.urls import reverse
# Create your models here.


class Math_score(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        blank= True, 
        null=True,
        related_name='players'
    )
    operator = models.CharField(max_length=50)
    max_range = models.SmallIntegerField(default=2)
    score = models.IntegerField(default=0)
    point = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
       ordering = ["-point"]
       

    def __str__(self):
        return self.operator

class Addition_score(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        blank= True, 
        null=True,
        related_name='players'
    )
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )
    max_range = models.SmallIntegerField(default=2)
    score = models.IntegerField(default=0)
    point = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('math_game:Addition', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)

    class Meta:
       ordering = ["-point"]
       
    def __str__(self):
        return self.operator
