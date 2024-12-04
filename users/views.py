from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView
from config import settings
from users.commands import generate_password
from users.forms import UserProfileForm, UserRegisterForm, PasswordResetForm
from users.models import User
from django.core.mail import send_mail
import random
from django.views.generic import FormView
from users.forms import VerificationForm
from django.contrib.auth.hashers import make_password


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    
    def form_valid(self, form):
        if form.is_valid():
            confirmation_code = random.randint(10000, 99990)
            send_mail(
                'Код подтверждения регистрации',
                f'Ваш код подтверждения регистрации: {confirmation_code}.',
                settings.EMAIL_HOST_USER,
                [form.cleaned_data.get('email')],
                fail_silently=False,
            )
            
            user = form.save(commit=False)
            user.verification_code = confirmation_code
            user.save()
            
        return redirect(reverse('users:login'))
            
    
class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')
    
    def get_object(self, query_set=None):
        return self.request.user

class VerificationFormView(FormView):
    template_name = 'users/verification.html'
    form_class = VerificationForm
    success_url = reverse_lazy('users:profile')

    def form_valid(self, form):
        if form.is_valid():
            confirmation_code = form.cleaned_data['confirmation_code']
            user = self.request.user

            if user.verification_code == confirmation_code:
                user.is_verified = True
                user.save()
                return super().form_valid(form)
            else:
                # Handle invalid verification code
                return render(self.request, 'users/verification_failed.html')
        
        
class PasswordResetView(FormView):
    template_name = 'users/password_reset.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('users:login')
    
    def form_valid(self, form):
        if form.is_valid():
            user = self.request.user
            new_password  = ''.join([str(random.randint(0, 9)) for string in range(10)])
            if user.email == form.cleaned_data['email']:
                send_mail(
                    'Новый пароль',
                    f'Ваш новый пароль: {new_password}.',
                    settings.EMAIL_HOST_USER,
                    [form.cleaned_data.get('email')],
                    fail_silently=False,
                )
                user.set_password(new_password)
                user.save()
                return super().form_valid(form)
            else:
                return redirect(reverse('users:login'))            
    