from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from .models import Product, ProductCategory
links_menu = [
        {'href': 'main', 'name': 'главная страница'},
        {'href': 'products:index', 'name': 'Продукция'},
        {'href': 'contact', 'name': 'контакты'},

]
same_products = [

]

def main(request):
    content = {
        'titles': 'главная страница',
        'links_menu': links_menu
    }
    return render(request, 'mainapp/index.html', context=content)

def index(request):


    content = {
        'titles': 'Продукты',
        'links_menu': links_menu,
        'category_menu': ProductCategory.objects.all(),
        'same_products': same_products
    }
    return render(request, 'mainapp/products.html', context=content)



def products(request, pk=None):
    if (pk != None):
        products = Product.objects.filter(category_id=pk).all()
    else:
        products = Product.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk:
        if pk == '0':
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')
    content = {
        'titles': 'Продукты',
        'links_menu': links_menu,
        'category_menu': ProductCategory.objects.all(),
        'products': products,
        'basket': basket
    }
    return render(request, 'mainapp/products.html', context=content)



def contact(request):
    content = {
        'titles': 'Контакты',
        'links_menu': links_menu
    }
    return render(request, 'mainapp/contact.html', context=content)

