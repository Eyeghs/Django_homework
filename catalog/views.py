from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    # функция принимает параметр request
    # и с помощью специальной функции возвращает ответ
    return render(request, 'catalog/index.html')

def contact_info(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'У вас новое сообщение от {name}({email}): {message}')
    return render(request, 'catalog/contacts.html')

def product(request):
    products_list = Product.objects.all()
    context = {'object_list': products_list}
    return render(request, 'catalog/product.html', context)
