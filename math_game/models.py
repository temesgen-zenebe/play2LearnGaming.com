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
       paginate_by: 5

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
    