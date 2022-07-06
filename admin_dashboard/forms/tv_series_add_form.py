from django import forms
from django.forms import ModelForm
from contents.models.content import TvSeries
from contents.models.country import Country
from contents.models.genre import Genre



class AddTvSeriesForm(ModelForm):
    """Content add form class definition """

    class Meta:
        model = TvSeries
        fields = '__all__'

    FULL_HD = 'full_hd'
    HD = 'hd'
    SD = 'sd'
    VID_QUALITY = (
        (FULL_HD, 'Full HD'),
        (HD, 'HD'),
        (SD, 'SD'),
    )

    cover_photo = forms.ImageField(widget=forms.FileInput(attrs={'accept': ".png, .jpg, .jpeg",
                                                                 'id': 'form__img-upload'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form__input',
                                                          'id': 'movie-title',
                                                          'placeholder': 'Name of the new series'}))
    descriptions = forms.CharField(widget=forms.Textarea(attrs={'class': 'form__textarea', 'placeholder': 'Enter '
                                                                                                          'series '
                                                                                                          'description'}))
    release_year = forms.CharField(widget=forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Release '
                                                                                                        'year'}))
    runtime = forms.CharField(widget=forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Runtime'}))
    video_quality = forms.ChoiceField(choices=VID_QUALITY,
                                      widget=forms.Select(
                                          attrs={'class': 'js-example-basic-single', 'id': 'quality'}))
    audience_age = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Age', 'class': 'form__input'}))
    country = forms.ModelMultipleChoiceField(queryset=Country.objects.all(),
                                             widget=forms.SelectMultiple(
                                                 attrs={'class': 'js-example-basic-multiple', 'id': 'country',
                                                        'multiple': 'multiple'}))
    genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(),
                                           widget=forms.SelectMultiple(
                                               attrs={'class': 'js-example-basic-multiple',
                                                      'id': 'genre', 'multiple': 'multiple'}))
