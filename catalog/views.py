from django.shortcuts import render
from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class ProductListView(ListView):
    """Контроллер главной страницы"""
    model = Product
    template_name = 'catalog/home.html'
    # def get_queryset(self, *args, **kwargs):
    #     """Отображение только 5 последних добавленных товаров"""
    #     queryset = super().get_queryset(*args, **kwargs)
    #     queryset = queryset.all()
    #     queryset = list(reversed(queryset))
    #     return queryset[:5]
# def home(request):
#     """Контроллер домашней страницы"""
#     product_list = Product.objects.all()
#     context = {
#         'object_list': product_list,
#         'title': 'Главная страница'
#     }
#     return render(request, 'catalog/home.html', context)


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


class ProductDetailView(DetailView):
    """Контроллер страницы товара"""
    model = Product
    template_name = 'catalog/product_card.html'
# def product_card(request, pk):
#     """Контроллер карточки товара"""
#     context = {
#         'object_list': Product.objects.filter(pk=pk),
#         'title': 'Product Card'
#     }
#     return render(request, 'catalog/product_card.html', context)
# В прошлый контроллер product в контекст передавалась коллекция объектов
# DetailView отдаёт в контекст только один объект - object, по которому нельзя итерироваться
# В шаблоне нужно убрать цикл и закрывающий тег, а object_list на object


class ProductCreateView(CreateView):
    """Контроллер страницы добавления товара от пользователя"""
    model = Product
    fields = ('product_name', 'product_description', 'product_image',
              'product_category', 'product_price', 'product_date_of_creation', 'product_date_of_change',)
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('product_name', 'product_description', 'product_image',
              'product_category', 'product_price', 'product_date_of_creation', 'product_date_of_change',)
    success_url = reverse_lazy('catalog:home')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')
