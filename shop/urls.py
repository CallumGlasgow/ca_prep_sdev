from django.urls import path
from .views import ProductCreateView, ProductDetailView, ProductListView, ProductDeleteView

urlpatterns =[
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/',ProductDetailView.as_view() , name ='product_detail'),

    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),    

]