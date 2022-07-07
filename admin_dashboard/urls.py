from django.urls import path
from admin_dashboard.views.admin_index import AdminIndex
from admin_dashboard.views.contents import AddContent, AddContentMF
from admin_dashboard.views.tv_series import TvSeriesAddView
from admin_dashboard.views.season_episode import AddSeasonView

app_name = 'admin_dashboard'
urlpatterns = [
    path('', AdminIndex.as_view(), name='admin-index'),
    # content
    path('add-content/', AddContent.as_view(), name='add-content'),
    path('add-content-mf/', AddContentMF.as_view(), name='add-content-mf'),
    # tv-series
    path('add-series/', TvSeriesAddView.as_view(), name='add-series'),
    path('add-season/', AddSeasonView.as_view(), name='add-season')

]
