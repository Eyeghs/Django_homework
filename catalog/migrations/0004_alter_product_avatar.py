# Generated by Django 5.1.2 on 2024-12-02 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_product_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='avatar',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Изображение'),
        ),
    ]
