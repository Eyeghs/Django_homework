from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import Product, Blog
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from django.shortcuts import get_object_or_404, redirect
# Create your views here.

def contact_info(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'У вас новое сообщение от {name}({email}): {message}')
    return render(request, 'catalog/contacts.html')

class ProductCreateView(CreateView):
    model = Product
    fields = ('product_name', 'description', 'category', 'price_for_one', 'avatar')
    success_url = reverse_lazy('catalog:index')
    
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')
    
class ProductDetailView(DetailView):
    model = Product
    
class ProductListView(ListView):
    model = Product
    
class ProductUpdateView(UpdateView):
    model = Product
    fields = ('product_name', 'description', 'category', 'price_for_one', 'avatar')
    success_url = reverse_lazy('catalog:index')
    
class BlogCreateView(CreateView):
    model = Blog
    fields = ('header', 'body', 'preview')
    success_url = reverse_lazy('catalog:blog_index')
    
    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.header)
            new_mat.save()
        return super().form_invalid(form)
    
class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_index')
    
class BlogDetailView(DetailView):
    model = Blog
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object
    
class BlogListView(ListView):
    model = Blog
    
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset

    
class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('header', 'body', 'preview')
    
    def get_success_url(self):
        return reverse_lazy('catalog:blog_view', kwargs={'pk': self.object.pk})

def toggle_activity(request, pk):
    blog_item = get_object_or_404(Blog, pk=pk)
    if blog_item.is_published:
        blog_item.is_published = False
    else:
        blog_item.is_published = True
    blog_item.save()
    return redirect(reverse('catalog:blog_index'))