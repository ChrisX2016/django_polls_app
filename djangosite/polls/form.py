from django import forms
from django.forms import ModelForm
from .models import UserProfile
from django.contrib.auth.models import User


class RegisterForm(ModelForm):
    error_css_class = 'error'
    firstname = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class':"form-control",'placeholder':"First Name"}))
    lastname = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class':"form-control",'placeholder':"Last Name"}))
    email = forms.EmailField(label='Email Address',widget=forms.TextInput(attrs={'class':"form-control",'placeholder':"Email"}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Password"}))
    password1 = forms.CharField(label='Verify Password',widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Verify Password"}))


    class Meta:
        model = UserProfile
        fields = ('username','birthday',)
        widgets = {
            'username': forms.TextInput(attrs={'class':"form-control",'placeholder':"Username"}),
            'birthday': forms.TextInput(attrs={'class':"form-control",'placeholder':"Birthday"}),
        }


    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("username exist")

    def clean_password_password1(self):
        password = self.cleaned_data['password']
        password1 = self.cleaned_data['password1']
        if password != password1:
            raise forms.ValidationError("Passwoed did not match")
        return password


