from django.shortcuts import render

# Create your views here.
from catalog.models import Product


def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Новые товары',
        'about': 'Последние поступления товаров представлены ниже. Странно сформулировано, да?'
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    context = {
        'title': 'Наши контакты',
        'about': ''
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'catalog/contacts.html', context)


def product(request, pk):
    show_product = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.get(pk=pk),
        'title': f'В продаже: {show_product.name}',
    }
    return render(request, 'catalog/product.html', context)
