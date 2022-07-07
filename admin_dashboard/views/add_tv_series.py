from django.views import generic
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from contents.models.content import TvSeries,TvSeriesGallery
from admin_dashboard.forms.tv_series_add_form import AddTvSeriesForm


class TvSeriesAddView(SuccessMessageMixin, generic.CreateView):
    model = TvSeries
    template_name = 'main/tvseries/tvseries_add.html'
    form_class = AddTvSeriesForm
    success_url = reverse_lazy('admin_dashboard:add-series')
    success_message = 'Tv Series created !'

    def form_valid(self, form):
        form.save()
        print()
        for photo in self.request.FILES.getlist('gallery'):
            TvSeriesGallery.objects.create(series=form.instance,series_image=photo)
        return super(TvSeriesAddView, self).form_valid(form)

