from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.coffee_add, name='coffee_add'),
    path('delete/<int:pk>/', views.coffee_delete, name='coffee_delete'),
]