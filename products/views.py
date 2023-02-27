from django.shortcuts import render, redirect
from .forms import CreateProduct
from .models import Product
# Create your views here.

def index(request):

    result = Product.objects.all().order_by('-id')

    return render(request, 'products/index.html', context={'products': result})



def create_product(request):


    if request.method == 'POST':
        product = CreateProduct(request.POST)

        if product.is_valid():
            product.save()
            return redirect('home')
    else:
        product = CreateProduct()

    return render(request, 'products/create.html', context={'product': product})
