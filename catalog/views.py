from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import Product, Blog, Version
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from django.shortcuts import get_object_or_404, redirect
from .forms import ProductForm, VersionForm
from django.forms import inlineformset_factory
from django.db.models import Prefetch
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def contact_info(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'У вас новое сообщение от {name}({email}): {message}')
    return render(request, 'catalog/contacts.html')

class ProductCreateView(LoginRequiredMixin ,CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog_index')
    
    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save(commit=False)
            user = self.request.user.email
            new_product.user_creator = user
            new_product.save()
        return super().form_valid(form)
    
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:catalog_index')
    
class ProductDetailView(DetailView):
    model = Product
    
class ProductListView(ListView):
    model = Product
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.prefetch_related(
            Prefetch('version_set', queryset=Version.objects.filter(version_state=True))
        )
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products_with_versions = []
        for product in context['object_list']:
            current_version = product.version_set.first()  # Получаем текущую версию (если есть)
            products_with_versions.append({
                'product': product,
                'current_version': current_version
            })
        context['products_with_versions'] = products_with_versions
        return context
    
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog_index')
    
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectForset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectForset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectForset(instance=self.object)
        return context_data
    
    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        
        return super().form_valid(form)
    
class BlogCreateView(CreateView):
    model = Blog
    fields = ('header', 'body', 'preview')
    success_url = reverse_lazy('catalog:blog_index')
    
    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.header)
            new_mat.save()
        return super().form_valid(form)
    
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