from django import forms
from django.forms import ModelForm
from contents.models.content import TvSeries
from contents.models.season_episode import Season, Episode


class SeasonAddForm(ModelForm):
    class Meta:
        model = Season
        fields = '__all__'

    tv_series = forms.ModelChoiceField(queryset=TvSeries.objects.all(),
                                       widget=forms.Select(
                                           attrs={'class': 'js-example-basic-simple', 'id': 'tvseries'}))
    season_title_or_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form__input',
                                                                           'id': 'movie-title',
                                                                           'placeholder': 'Season Title / Season '
                                                                                          'number '}))
    season_description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form__textarea', 'placeholder': 'Enter '
                                                                               'Season '
                                                                               'description'}))
