from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User
from django import forms

class UserRegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
        
class UserProfileForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar', 'country')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['password'].widget = forms.HiddenInput()
        
class VerificationForm(forms.Form):
    confirmation_code = forms.CharField(max_length=6)
    
class PasswordResetForm(forms.Form):
    email = forms.CharField(max_length=254)