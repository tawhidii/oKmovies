from .common import AbstractItemModel


class Category(AbstractItemModel):
    """Category model definition """

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
