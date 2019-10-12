"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home_page, about_us, contact_us, login_page, signup_page, logout_page
from django.conf.urls.static import static
from django.conf import settings
from products.views import product_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name = 'home'),
    path('product/', product_list, name = 'products'),
    path('contact/', contact_us, name = 'contact'),
    path('login/', login_page, name = 'login'),
    path('logout/', logout_page, name = 'logout'),
    path('signup/', signup_page, name = 'register'),
    path('about/', about_us, name = 'about'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
