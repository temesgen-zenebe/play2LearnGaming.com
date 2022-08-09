from asyncio.windows_events import NULL
from django.db import models
from django.conf import settings
from django.utils.timezone import datetime
from common.utils.text import unique_slug
from django.urls import reverse
from django.utils import timezone

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
        