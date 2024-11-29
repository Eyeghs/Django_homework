from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    avatar = models.ImageField(upload_to='products', verbose_name='Изображение')
    category = models.CharField(max_length=50, verbose_name='Категория')
    price_for_one = models.IntegerField(verbose_name='Цена за штуку')
    creation_date = models.DateField(verbose_name='Дата создания продукта')
    last_change_date = models.DateField(verbose_name='Дата последнего изменения')
    
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