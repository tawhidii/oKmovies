from django.db import models
from .common import ContentCommonModel
from core.models import TimeStampedModel
from .genre import Genre
from .country import Country
from .category import Category


class Content(ContentCommonModel, TimeStampedModel):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='content')
    genre = models.ManyToManyField(Genre, related_name='contents')
    country = models.ManyToManyField(Country, related_name='contents')
    video_url = models.URLField(verbose_name='Content media url',default='https://www.youtube.com/')

    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Contents'

    def __str__(self):
        return self.title
