from django.shortcuts import render

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
    return render(request, 'catalog/contact.html')
