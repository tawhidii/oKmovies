from django.shortcuts import render, redirect
from django.views.generic import View
from contents.models.country import Country
from contents.models.genre import Genre
from contents.models.content import Content
from contents.models.category import Category


class AddMovie(View):

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
        movie_cover = request.FILES.get('form__img-upload')
        movie_title = request.POST.get('title')
        movie_description = request.POST.get('description')
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
        print(movie_cover)

        movie_object = Content.objects.create(cover_photo=movie_cover,title=movie_title, descriptions=movie_description,
                                              release_year=release_year, runtime=runtime,
                                              video_quality=video_quality,
                                              audience_age=audience_age,
                                              video_url=video_url,category_id=int(category_id))

        movie_object.genre.set(genre_list)
        movie_object.country.set(country_list)
        movie_object.save()

        return redirect('admin_dashboard:add-movie')
