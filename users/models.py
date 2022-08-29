from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings

from django.utils import timezone

def validate_avatar(value):
    w, h = get_image_dimensions(value)
    if w > 200 or h > 200:
        raise ValidationError('Avatar must be no bigger than 200x200 pixels.')

# Create your models here.
class CustomUser(AbstractUser):
    
    dob = models.DateField(
        verbose_name= "Date of Birth", null=True , blank=True
    )
    avatar = models.ImageField(
        upload_to='avatars/', 
        blank=True,
        help_text='Image must be 200px by 200px.',
        validators=[validate_avatar],
    )
    
    def get_absolute_url(self):
        return reverse('my-account')

    def __str__(self):
        return f'{self.username}'
    
    


