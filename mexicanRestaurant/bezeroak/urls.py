from django.template.defaulttags import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.bezeroak_index, name='bezeroak_index'),

    #path(r'^salg', views.index, name='index'),
]
