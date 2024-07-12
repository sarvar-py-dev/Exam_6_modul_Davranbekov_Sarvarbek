from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from apps.models import Product
from apps.task import send_to_email


class ProductListView(ListView):
    model = Product
    template_name = 'apps/product/product-list.html'
    context_object_name = 'product_list'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'apps/product/product-detail.html'
    context_object_name = 'product_detail'


class RegisterCreateView(CreateView):
    template_name = 'apps/auth/register.html'
    success_url = reverse_lazy('list_view')

    def form_valid(self, form):
        form.save()
        send_to_email().delay('Ro`yhattan o`tganingiz uchun rahmat', form.data['email'])
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class UserLoginView(LoginView):
    template_name = 'apps/auth/login.html',
    redirect_authenticated_user = True,
    next_page = 'list_view'

    def form_valid(self, form):
        send_to_email.delay('Saytimizga xush kelibsiz', form.data['email'])
        return super().form_valid(form)


class ProductCreateView(CreateView):
    template_name = 'apps/product/product-create.html'
    model = Product
    fields = 'video', 'name', 'description', 'is_premium'


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'apps/product/product-update.html'
    fields = 'name', 'description', 'video', 'is_premium'


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('list_view')
