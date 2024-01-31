from django.urls import path
from catalog.views import (contacts, ProductListView, ProductDetailView,
                           ProductCreateView, ProductUpdateView, ProductDeleteView)
from catalog.apps import CatalogConfig
from django.views.decorators.cache import cache_page

app_name = CatalogConfig.name


urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('view/<int:pk>/product_card/', cache_page(60)(ProductDetailView.as_view()), name='product_card'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('edit/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    ]
