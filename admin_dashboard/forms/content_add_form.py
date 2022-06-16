from django import forms
from django.forms import ModelForm
from contents.models.content import Content
from contents.models.country import Country
from contents.models.genre import Genre
from contents.models.category import Category


class AddContentForm(ModelForm):
    """Content add form class definition """

    class Meta:
        model = Content
        fields = ('cover_photo', 'title', 'descriptions', 'release_year',
                  'runtime', 'video_quality', 'audience_age', 'category', 'country', 'genre', 'video_url',)

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
                                                          'placeholder': 'Content Title'}))
    descriptions = forms.CharField(widget=forms.Textarea(attrs={'class': 'form__textarea', 'placeholder': 'Enter '
                                                                                                          'content '
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
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      widget=forms.Select(
                                          attrs={'class': 'js-example-basic-simple', 'id': 'category'}))
    video_url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form__input'}),
                               initial='Ex: https://www.youtube.com/')

    def save(self, *args, **kwargs):
        content = super().save(commit=False)
        content.cover_photo = self.cleaned_data.get('cover_photo')
        content.title = self.cleaned_data.get('title')
        content.descriptions = self.cleaned_data.get('descriptions')
        content.release_year = self.cleaned_data.get('release_year')
        content.runtime = self.cleaned_data.get('runtime')
        content.video_quality = self.cleaned_data.get('video_quality')
        content.audience_age = self.cleaned_data.get('audience_age')
        content.category_id = self.cleaned_data.get('category').id
        content.video_url = self.cleaned_data.get('video_url')
        content.save()
        countries = [int(c.id) for c in self.cleaned_data.get('country')]
        genres = [int(g.id) for g in self.cleaned_data.get('genre')]
        content.country.set(countries)
        content.genre.set(genres)

        return content
