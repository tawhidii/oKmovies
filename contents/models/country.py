from .common import AbstractItemModel


class Country(AbstractItemModel):
    """Country model definition """

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name
