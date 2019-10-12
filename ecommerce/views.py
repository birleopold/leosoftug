from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import contactForm, loginForm, signup

def home_page(request):

    return render(request, 'index.html')


def about_us(request):
    context = {'title': 'about us page',
    'content':'welcome enjoy browsing the site'
    }

    return render(request, 'home.html', context)


def contact_us(request):
    contactusForm = contactForm(request.POST or None)
    context = {'title':'Please contact us here',
    'content':'welcome enjoy browsing the site',
    'form':contactusForm
    }
    if contactusForm.is_valid():
        context['form']= contactForm

    return render(request, 'contact.html', context)

def login_page(request):
    form = loginForm(request.POST or None)
    context = {
    'form':form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not  None:
            login(request, user)
            context['form'] = loginForm
            return redirect("/login")
        else:
            print ('Error')

    return render(request, 'auth/login.html', context)

user = get_user_model()
def signup_page(request):
    signup_ = signup(request.POST or None)
    context = {
    'form':signup_
    }
    if signup_.is_valid():
        first_name = signup_.cleaned_data.get("firstname")
        last_name = signup_.cleaned_data.get("lastname")
        username = signup_.cleaned_data.get("username")
        email = signup_.cleaned_data.get("email")
        password = signup_.cleaned_data.get("password")
        extra_fields = {'first_name':first_name, 'last_name':last_name}
        new_user = user.objects.create_user(username, email, password, **extra_fields)

        context['form'] = signup
    return render(request, 'auth/signup.html', context)

def logout_page(request):
    logout(request)
