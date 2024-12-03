from django import forms
from .models import Product, Version

prohibited_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар', 'Казино', 'Криптовалюта', 'Крипта', 'Биржа', 'Дешево', 'Бесплатно', 'Обман', 'Полиция', 'Радар']

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ('product_name', 'description', 'category', 'price_for_one', 'avatar')
        
    def clean_product_name(self):
        cleaned_data = self.cleaned_data.get('product_name')
        
        if cleaned_data in prohibited_words:
            raise forms.ValidationError('Недопустимое название продукта')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        if cleaned_data in prohibited_words:
            raise forms.ValidationError('Недопустимое описание продукта')
        return cleaned_data
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
class VersionForm(forms.ModelForm):
    
    class Meta:
        model = Version
        fields = ('product', 'version_number', 'version_name',)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'