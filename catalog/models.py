from django.db import models
from django.utils import timezone



class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    avatar = models.ImageField(upload_to='products/', verbose_name='Изображение', null=True, blank=True)
    category = models.CharField(max_length=50, verbose_name='Категория')
    price_for_one = models.IntegerField(verbose_name='Цена за штуку')
    creation_date = models.DateField(verbose_name='Дата создания продукта', default=timezone.now)
    last_change_date = models.DateField(verbose_name='Дата последнего изменения', null=True, blank=True)
    
    def __str__(self):
        return f'{self.product_name}, {self.description}'
    
    
    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('product_name',)
        
class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    
    def __str__(self):
        return f'{self.category_name} {self.description}'
    
    
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('category_name',)
        
class Blog(models.Model):
    header = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, verbose_name='Slug', null=True, blank=True)
    body = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blogs/', verbose_name='Изображение', null=True, blank=True)
    creation_date = models.DateField(verbose_name='Дата создания продукта', default=timezone.now)
    is_published = models.BooleanField(verbose_name='Признак публикации', default=True)
    views_count = models.PositiveIntegerField(verbose_name='Количество просмотров', default=0)
    
    def __str__(self):
        return f'{self.header}, {self.body}'
    
    
    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ('header',)