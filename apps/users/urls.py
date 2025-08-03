from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user-list'),
    path('create/', views.register_user, name='user-register'),
    path('login/', views.login_user, name='user-login'),
    path('details/', views.update_user_details, name='user-update'),
]