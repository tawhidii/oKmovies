from django.urls import path
from .views import AdminIndex

app_name = 'admin_dashboard'
urlpatterns = [
    path('', AdminIndex.as_view(), name='admin-index')
]
