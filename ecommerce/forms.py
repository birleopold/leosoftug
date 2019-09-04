from django import forms


class contactForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control', 'id':'form_full_name', 'placeholder':'your full name'}))
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class':'form-control', 'placeholder':'abcd@efg.com'}))
    content = forms.CharField(widget = forms.Textarea(attrs ={'clcass':'form-control', 'placeholder':'your message here'}))


class loginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control', 'id':'form_full_name', 'placeholder':'username'}))
    password = forms.CharField(widget=forms.PasswordInput())


class signup(forms.Form):
    firstname = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control', 'id':'form_full_name', 'placeholder':'first name'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control', 'id':'form_full_name', 'placeholder':'last name'}))
    username = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control', 'id':'form_full_name', 'placeholder':'username'}))
    email = forms.CharField(widget = forms.EmailInput(attrs={'class':'form-control', 'placeholder':'abcd@efg.com'}))
    password = forms.CharField(widget=forms.PasswordInput())
