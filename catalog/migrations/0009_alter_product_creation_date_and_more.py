# Generated by Django 5.1.2 on 2024-12-03 07:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_product_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='creation_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_change_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата последнего изменения'),
        ),
    ]