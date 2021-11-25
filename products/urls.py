from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('like/<int:product_id>', views.like_product, name='like_product'),
    path('add_print/', views.add_print, name='add_print'),
    path('edit_print/<int:product_id>/', views.edit_print, name='edit_print'),
    path('delete_print/<int:product_id>/', views.delete_print,
         name='delete_print'),
    path('edit_printoption/<int:option_size>/', views.edit_printoption,
         name='edit_printoption'),
]
