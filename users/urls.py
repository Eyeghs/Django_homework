from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, VerificationFormView, PasswordResetView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('verification_form/', VerificationFormView.as_view(), name='verification_form'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
 ]