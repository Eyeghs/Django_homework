from django.urls import path
from catalog.views import index, contact_info

app_name = 'catalog'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact_info, name='contact_info'),
]