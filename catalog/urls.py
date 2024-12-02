from django.urls import path
from catalog.views import index, contact_info, product
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contact_info, name='contacts'),
    path('product/', product, name='product'),
]