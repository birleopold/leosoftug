from django import forms
from django.contrib.auth import get_user_model

user = get_user_model()
class contactForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control', 'id':'form_full_name', 'placeholder':'your full name'}))
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class':'form-control', 'placeholder':'abcd@efg.com'}))
    content = forms.CharField(widget = forms.Textarea(attrs ={'clcass':'form-control', 'placeholder':'your message here'}))


class loginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control', 'id':'form_full_name', 'placeholder':'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs = {'class':'form-control', 'id':'form_full_name', 'placeholder':'password'}))


class signup(forms.Form):
    firstname = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control', 'id':'form_full_name', 'placeholder':'first name'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control', 'id':'form_full_name', 'placeholder':'last name'}))
    username = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control', 'id':'form_full_name', 'placeholder':'username'}))
    email = forms.CharField(widget = forms.EmailInput(attrs={'class':'form-control', 'placeholder':'abcd@efg.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs = {'class':'form-control', 'id':'form_full_name', 'placeholder':'password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs = {'class':'form-control', 'id':'form_full_name', 'placeholder':'confirm password'}))

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if confirm_password != password:
            raise forms.ValidationError('passwords dont match')
        else:
            return data

    def clean_email(self):
        data = self.cleaned_data
        email = self.cleaned_data.get('email')
        qs = user.objects.filter(email = email)
        if qs.exists():
            raise forms.ValidationError('email already taken')
        return email


    def clean_username(self):
        data = self.cleaned_data
        username = self.cleaned_data.get('username')
        qs = user.objects.filter( username = username)
        if qs.exists():
            raise forms.ValidationError('username already taken')
        else:
            return username
