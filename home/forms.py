from django import forms
from django.forms import ModelForm, TextInput, Textarea
from home.models import ContactFormMessage

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(
                attrs={'type': "text",'class': "form-control", 'id': "name", 'placeholder': "Your Name & Surname", 'required': "required",
                'data-validation-required-message ': "Please enter your name"}),
            
            'email': TextInput(
                attrs={'type': 'email', 'class': "form-control", 'id': "email", 'placeholder': "Your Email",
                'required': "required", 'data-validation-required-message': "Please enter your email"}),
            
            'subject': TextInput(
                attrs={'type': "text", 'class': "form-control", 'id': "subject", 'placeholder': "Subject",
                'required': "required", 'data-validation-required-message': "Please enter a subject"}),
            
            'message': Textarea(
                attrs={'class': "form-control", 'rows': "6", 'id': "message", 'placeholder': "Message",
                'required': "required",
                'data-validation-required-message': "Please enter your message"}),
        }

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
    # catid = forms.IntegerField()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)

    password = forms.CharField(widget=forms.PasswordInput())
    # catid = forms.IntegerField()

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30,label= 'User Name :')
    email = forms.EmailField(max_length=200,label= 'Email :')
    first_name = forms.CharField(max_length=100, help_text='First Name',label= 'First Name :')
    last_name = forms.CharField(max_length=100, help_text='Last Name',label= 'Last Name :')

    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name', 'password1', 'password2', )