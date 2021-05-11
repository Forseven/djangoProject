from django.shortcuts import render

links_menu = [
        {'href': 'index', 'name': 'главная страница'},
        {'href': 'products', 'name': 'продукты'},
        {'href': 'contact', 'name': 'контакты'},

]
same_products = [

]

def index(request):
    content = {
        'titles': 'главная страница',
        'links_menu': links_menu
    }
    return render(request, 'mainapp/index.html', context=content)

def products(request):
    content = {
        'titles': 'Продукты',
        'links_menu': links_menu,
        'same_products': same_products
    }
    return render(request, 'mainapp/products.html', context=content)


def contact(request):
    content = {
        'titles': 'Контакты',
        'links_menu': links_menu
    }
    return render(request, 'mainapp/contact.html', context=content)

