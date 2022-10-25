from .models import Product
from django.shortcuts import get_object_or_404,render


def products (request):

    context = {'products': Product.objects.all()}
    return render(request, 'products/products.html', context)


def product(request, pro_id):
    context = {
        'pro':get_object_or_404(Product,pk=pro_id)
    }
    return render(request, 'products/product.html', context)
