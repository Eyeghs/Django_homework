# Generated by Django 5.1.2 on 2024-12-02 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_category_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='products', verbose_name='Изображение'),
        ),
    ]
