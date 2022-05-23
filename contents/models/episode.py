from django.db import models
from .common import AbstractItemModel


class Episode(AbstractItemModel):
    media_url = models.URLField(verbose_name='Hosted Media Url')

    class Meta:
        verbose_name = 'Episode'
        verbose_name_plural = 'Episodes'

    def __str__(self):
        return self.name
