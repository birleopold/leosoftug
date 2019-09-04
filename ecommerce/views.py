from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import contactForm, loginForm, signup

def home_page(request):
    context = {'title':'Welcome to the our site',
    'content':'welcome enjoy browsing the site'
    }
    return render(request, 'home.html', context)


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
    loginform = loginForm(request.POST or None)
    context = {
    'form':loginform
    }

    if loginform.is_valid():
        username = loginform.cleaned_data.get('username')
        password = loginform.cleaned_data.get('password')
        user = authenticate(request, username=username, passwprd=password)
        if user is not  None:
            login(request, user)
            return redirect('login/')
        else:
            print ('error')

        context['form'] = loginForm

    return render(request, 'auth/login.html', context)

def signup_page(request):
    signup_ = signup(request.POST or None)
    context = {
    'form':signup_
    }
    return render(request, 'auth/signup.html', context)
