from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('newProduct/', views.newProduct),
    path('edit/<int:id>', views.edit),
    path('delete/<int:id>', views.delete),
]
