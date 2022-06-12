from django.db import models


class ContentCommonModel(models.Model):
    """ Common fields for contents(Ex. movies and tv-series) model definition """
    FULL_HD = 'full_hd'
    HD = 'hd'
    SD = 'sd'
    VID_QUALITY = (
        (FULL_HD, 'Full HD'),
        (HD, 'HD'),
        (SD, 'SD'),
    )
    cover_photo = models.ImageField(upload_to='movies/%Y/%m/%d/')
    title = models.CharField(max_length=150)
    descriptions = models.TextField()
    release_year = models.CharField(max_length=5, help_text='Enter Release Year')
    runtime = models.CharField(max_length=15, help_text='Runtime must be in minutes',blank=True,null=True)
    video_quality = models.CharField(max_length=8, choices=VID_QUALITY, default=FULL_HD)
    audience_age = models.PositiveIntegerField(default=13)

    class Meta:
        abstract = True


class AbstractItemModel(models.Model):
    """ Model definition abstract item"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    class Meta:
        abstract = True
