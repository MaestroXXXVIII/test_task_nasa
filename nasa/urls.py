from django.urls import path

from . import views

urlpatterns = [
    path('', views.slider_list, name='slider_list'),
]