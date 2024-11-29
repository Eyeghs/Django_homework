from django.core.management import BaseCommand, call_command
import os
from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        
        file_path = os.path.join(os.getcwd(), 'catalog_data.json')
        call_command('dumpdata', 'catalog.Product', 'catalog.Category', '--output', file_path)
        
        