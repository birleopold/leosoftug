from django.shortcuts import render
from .models import Product

# Create your views here.
def product_list(request):
    query_set = Product.objects.all()
    context = {
    'product_list' : query_set
    }
    return render(request, 'product/product.html', context)
