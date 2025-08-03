from django.urls import path
from . import views

urlpatterns = [
    path('', views.supplier_list, name='supplier-list'),
    path('create/', views.create_supplier, name='supplier-create'),
]