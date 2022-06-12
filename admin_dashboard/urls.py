from django.urls import path
from admin_dashboard.views.admin_index import AdminIndex
from admin_dashboard.views.add_movies import AddMovie

app_name = 'admin_dashboard'
urlpatterns = [
    path('', AdminIndex.as_view(), name='admin-index'),
    path('add-movie/', AddMovie.as_view(), name='add-movie')
]
