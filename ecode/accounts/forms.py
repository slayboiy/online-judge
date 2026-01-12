from django import forms
from django.contrib.auth.models import User

class SignUp(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput
    )
    
    class Meta:
        model = User
        fields = ["username", "email"]
    
    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("password1")
        p2 = cleaned_data.get("password2")
        
        if p1 and p2 and p1 != p2:
            self.add_error("password2", "Пароли не совпадают")
        
        return cleaned_data
    