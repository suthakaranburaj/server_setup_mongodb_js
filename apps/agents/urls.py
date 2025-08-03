from django.urls import path
from . import views

urlpatterns = [
    path('', views.agent_list, name='agent-list'),
    path('create/', views.create_agent, name='agent-create'),
]