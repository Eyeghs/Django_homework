from django.urls import path
from catalog.views import contact_info
from catalog.apps import CatalogConfig
from catalog.views import ProductCreateView, ProductListView, ProductDeleteView, ProductDetailView, ProductUpdateView
from catalog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView, toggle_activity

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', contact_info, name='contacts'),
    
    path('', ProductListView.as_view(), name='catalog_index'),
    path('view/<int:pk>', ProductDetailView.as_view(), name='view_product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    path('edit/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    
    path('blogs/', BlogListView.as_view(), name='blog_index'),
    path('blogs/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blogs/delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
    path('blogs/edit/<int:pk>', BlogUpdateView.as_view(), name='blog_update'),
    path('blogs/view/<int:pk>', BlogDetailView.as_view(), name='blog_view'),
    path('activity/<int:pk>', toggle_activity, name='toggle_activity'),
]
