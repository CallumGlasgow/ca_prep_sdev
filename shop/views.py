from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import DetailView, ListView
from .models import Product
from django.urls import reverse_lazy
# Create your views here.

class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_create.html'
    fields = ['name', 'price']
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
    



    