from django.contrib import admin
from contents.models import content
from contents.models import genre
from contents.models import country
from contents.models import category
from contents.models import season_episode


@admin.register(content.Content)
class ContentAdmin(admin.ModelAdmin):
    """Movie admin class definition"""
    pass


@admin.register(genre.Genre)
class GenreAdmin(admin.ModelAdmin):
    """Genre admin class definition"""
    prepopulated_fields = {'slug': ('name',)}


@admin.register(country.Country)
class CountryAdmin(admin.ModelAdmin):
    """Country Admin class definition """
    prepopulated_fields = {'slug': ('name',)}


@admin.register(category.Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category admin class Definition """
    prepopulated_fields = {'slug': ('name',)}


@admin.register(season_episode.Season)
class SeasonAdmin(admin.ModelAdmin):
    """Season Admin admin Definition """
    pass


@admin.register(season_episode.Episode)
class EpisodeAdmin(admin.ModelAdmin):
    """Episode admin class definition  """
    pass


@admin.register(content.TvSeries)
class TvSeriesAdmin(admin.ModelAdmin):
    """Tv Series admin class definition """
    pass


@admin.register(content.ContentGallery)
class ContentGalleryAdmin(admin.ModelAdmin):
    """ Content Gallery admin class definition"""
    pass
