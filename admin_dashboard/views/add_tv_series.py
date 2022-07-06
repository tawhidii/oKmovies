from django.views import generic
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from contents.models.content import TvSeries
from admin_dashboard.forms.tv_series_add_form import AddTvSeriesForm


class TvSeriesAddView(SuccessMessageMixin,generic.CreateView):
    model = TvSeries
    template_name = 'main/tvseries/tvseries_add.html'
    form_class = AddTvSeriesForm
    success_url = reverse_lazy('admin_dashboard:add-series')
    success_message = 'Tv Series created !'
