from django.contrib import admin
from . models import Category, Product, Version

# Register your models here.
@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    search_fields = ('category_name', )
    
@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price_for_one', 'category')
    list_filter = ('category',)
    search_fields = ('product_name', 'description')
    
@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'version_number', 'version_name', 'version_state')
    search_fields = ('product', 'version_number')