from django.shortcuts import render, reverse
from catalog.models import Product, Version
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from catalog.forms import ProductForm, VersionForm
from django.forms import inlineformset_factory
from catalog.service import check_user
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
# @login_required - для закрытия контроллера логином, для классов LoginRequiredMixin


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
        send_mail(
            'Сообщение от пользователя',
            f'Пользователь:{name}\nТелефон:{phone}\nСообщение:{message}',
            EMAIL_HOST_USER,
            ['kettariec@gmail.com']
        )
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


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Контроллер страницы добавления товара от пользователя"""
    model = Product
    form_class = ProductForm
    # fields = ('product_name', 'product_description', 'product_image',
    #           'product_category', 'product_price', 'product_date_of_creation', 'product_date_of_change',)

    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        """Добавление автора к товару"""
        self.object = form.save()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(UserPassesTestMixin, UpdateView):
    """Контроллер страницы редактирования товара"""
    model = Product
    form_class = ProductForm
    # fields = ('product_name', 'product_description', 'product_image',
    #           'product_category', 'product_price', 'product_date_of_creation', 'product_date_of_change',)

    def test_func(self):
        user = self.request.user
        author = self.get_object().author
        if check_user(user, author):
            return True
        return self.handle_no_permission()

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    success_url = reverse_lazy('catalog:home')


class ProductDeleteView(UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')

    def test_func(self):
        if self.request.user == self.get_object().author or self.request.user.is_superuser is True:
            return True
        return self.handle_no_permission()
