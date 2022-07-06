from django.db import models
from .common import ContentCommonModel
from core.models import TimeStampedModel
from .genre import Genre
from .country import Country
from .category import Category


class Content(ContentCommonModel, TimeStampedModel):
    cover_photo = models.ImageField(upload_to='contents/%Y/%m/%d/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='content')
    genre = models.ManyToManyField(Genre, related_name='contents')
    country = models.ManyToManyField(Country, related_name='contents')
    video_url = models.URLField(verbose_name='Content media url', default='https://www.youtube.com/')

    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Contents(ex. Movies,Cartoon,Documentary etc.)'

    def __str__(self):
        return self.title


class ContentGallery(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    content_image = models.ImageField(upload_to='movies/%Y/%m/%d/')

    class Meta:
        verbose_name = 'Content Gallery'
        verbose_name_plural = 'Content Gallery'

    def __str__(self):
        return self.content_image.url


class TvSeries(ContentCommonModel, TimeStampedModel):
    """TV Series Model definition """
    cover_photo = models.ImageField(upload_to='tvseries/%Y/%m/%d/')
    genre = models.ManyToManyField(Genre, related_name='tvseries')
    country = models.ManyToManyField(Country, related_name='tvseries')

    class Meta:
        verbose_name_plural = ' Tv Series'

    def __str__(self):
        return self.title


class TvSeriesGallery(models.Model):
    series = models.ForeignKey(TvSeries, on_delete=models.CASCADE)
    series_image = models.ImageField(upload_to='tv-series/%Y/%m/%d/')

    class Meta:
        verbose_name = 'Tv Series Gallery'
        verbose_name_plural = 'Tv Series Gallery'

    def __str__(self):
        return self.series_image.url
