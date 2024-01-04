from django.shortcuts import render
from catalog.models import Product


def home(request):
    """Контроллер домашней страницы"""
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Главная страница'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    """Контроллер страницы контактов"""
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # а также передается информация, которую заполнил пользователь
        print(name, phone, message)
    context = {
        'title': 'Contacts'
    }
    return render(request, 'catalog/contacts.html', context)


def product_card(request, pk):
    """Контроллер карточки товара"""
    context = {
        'object_list': Product.objects.filter(pk=pk),
        'title': 'Product Card'
    }
    return render(request, 'catalog/product_card.html', context)
