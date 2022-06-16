from django.urls import path
from admin_dashboard.views.admin_index import AdminIndex
from admin_dashboard.views.add_contents import AddContent, AddContentMF

app_name = 'admin_dashboard'
urlpatterns = [
    path('', AdminIndex.as_view(), name='admin-index'),
    path('add-movie/', AddContent.as_view(), name='add-content'),
    path('add-movie-mf/', AddContentMF.as_view(), name='add-content-mf')
]
