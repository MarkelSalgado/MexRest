from django.template.defaulttags import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('menu', views.menu, name='menu'),
    path('add_platera', views.add_platera, name='add_platera'),
    path('addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/', views.updaterecord, name='updaterecord'),

    #path(r'^salg', views.index, name='index'),
]
