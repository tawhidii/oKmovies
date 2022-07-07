from django.views import generic
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from contents.models.season_episode import Episode, Season
from admin_dashboard.forms.season_episode_form import SeasonAddForm


class AddSeasonView(SuccessMessageMixin,generic.CreateView):
    model = Episode
    template_name = 'main/tvseries/add_season.html'
    form_class = SeasonAddForm
    success_url = reverse_lazy('admin_dashboard:add-season')
    success_message = 'Added Episode !'

