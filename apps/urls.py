from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path

from apps.views import ProductListView, ProductDetailView, RegisterCreateView, ProductUpdateView, ProductCreateView, \
    ProductDeleteView, UserLoginView

urlpatterns = [
    path('', ProductListView.as_view(), name='list_view'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='detail_view'),
    path('login', UserLoginView.as_view(), name='login_page'),
    path('register', RegisterCreateView.as_view(), name='register_page'),
    path('product-update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product-create', ProductCreateView.as_view(), name='product_create'),
    path('product-delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete')
]
