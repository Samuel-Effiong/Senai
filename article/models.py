from django.db import models
from django.shortcuts import reverse
from django.utils import timezone


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='published_date')

    published_date = models.DateField(default=timezone.now)
    thumbnail = models.CharField(max_length=500, null=True, blank=True)

    category = models.CharField(max_length=20, editable=False, default='Article')

    def __str__(self):
        return f"{self.title} on {self.published_date}"

    class Meta:
        ordering = ('-published_date',)

    def get_absolute_url(self):
        return reverse('articles', args=[self.slug])


