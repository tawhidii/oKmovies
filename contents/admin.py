from django.contrib import admin
from contents.models import content
from contents.models import genre
from contents.models import country
from contents.models import category
from contents.models import episode


@admin.register(content.Content)
class MovieAdmin(admin.ModelAdmin):
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


