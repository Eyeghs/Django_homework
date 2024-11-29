from django.core.management import BaseCommand, call_command
import os
from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete
        
        file_path = os.path.join(os.getcwd(), 'catalog_data.json')
        call_command('loaddata', file_path)
        
        