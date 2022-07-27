from django.db import models
from django.conf import settings
from django.utils.timezone import datetime
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
    ranked = models.SmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
       ordering = ["-point"]

    def __str__(self):
        return self.operator
