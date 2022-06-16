from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import View, FormView
from django.contrib import messages
from contents.models.country import Country
from contents.models.genre import Genre
from contents.models.content import Content, ContentGallery
from contents.models.category import Category
from admin_dashboard.forms.content_add_form import AddContentForm

class AddContent(View):

    def get(self, request):
        template_name = 'main/add_movie.html'
        countries = Country.objects.all()
        genres = Genre.objects.all()
        categories = Category.objects.all()

        ctx = {
            'countries': countries,
            'genres': genres,
            'categories': categories
        }

        return render(request, template_name, ctx)

    def post(self, request):
        content_cover = request.FILES.get('form__img-upload')
        content_title = request.POST.get('title')
        content_description = request.POST.get('description')
        release_year = request.POST.get('release_year')
        runtime = request.POST.get('runtime')
        video_quality = request.POST.get('video_quality')
        audience_age = request.POST.get('audience_age')
        country = request.POST.getlist('country')
        genre = request.POST.getlist('genre')
        video_url = request.POST.get('video_url')
        category_id = request.POST.get('category')
        genre_list = [int(g) for g in genre]
        country_list = [int(c) for c in country]
        gallery_images = request.FILES.getlist('gallery')

        content_object = Content.objects.create(cover_photo=content_cover, title=content_title,
                                                descriptions=content_description,
                                                release_year=release_year, runtime=runtime,
                                                video_quality=video_quality,
                                                audience_age=audience_age,
                                                video_url=video_url, category_id=int(category_id))
        for image in gallery_images:
            ContentGallery.objects.create(content=content_object, content_image=image)

        content_object.genre.set(genre_list)
        content_object.country.set(country_list)
        content_object.save()
        messages.success(request, 'Content added successfully !!')
        return redirect('admin_dashboard:add-movie')


class AddContentMF(FormView):
    template_name = 'main/add_movie_model.html'
    form_class = AddContentForm
    success_url = reverse_lazy('admin_dashboard:add-content-mf')

    def form_valid(self, form):
        form.save()
        for photo in self.request.FILES.getlist('gallery'):
            ContentGallery.objects.create(content=form.instance, content_image=photo)
        messages.success(self.request, 'Content Added !!')
        return super().form_valid(form)
