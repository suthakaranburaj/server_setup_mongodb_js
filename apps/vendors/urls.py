from django.urls import path
from . import views

urlpatterns = [
    path('', views.vendor_list, name='vendor-list'),
    path('create/', views.create_vendor, name='vendor-create'),
]