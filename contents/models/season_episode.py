from django.db import models
from .content import TvSeries


class Season(models.Model):
    """Season model definition"""
    tv_series = models.ForeignKey(TvSeries, on_delete=models.CASCADE, related_name='seasons')
    season_title_or_number = models.CharField(max_length=150, unique=True,verbose_name='Season title or number')
    season_description = models.TextField()

    class Meta:
        verbose_name = 'Season'
        verbose_name_plural = 'Seasons'

    def __str__(self):
        return f'{self.tv_series.title}  | {self.season_title_or_number}'


class Episode(models.Model):
    """Episode Model Definition"""
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='episodes')
    episode_title = models.CharField(max_length=150, unique=True)
    media_url = models.URLField(verbose_name='Hosted Media Url')

    class Meta:
        verbose_name = 'Episode'
        verbose_name_plural = 'Episodes'

    def __str__(self):
        return self.episode_title
