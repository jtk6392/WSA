from django.urls import path

from . import views

urlpatterns = [
    path('', views.run),
    path('GUI/', views.gui, name='gui'),
    path('home/', views.index)
]