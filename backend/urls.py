from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('home/', views.index),
    path('GUI/', views.gui, name='gui'),
    path('app/', views.application)
]