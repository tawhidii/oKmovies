from .common import AbstractItemModel


class Genre(AbstractItemModel):
    """ Model Definition for genre"""
    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.name
