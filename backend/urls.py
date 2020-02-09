from django.urls import path

from . import apps
from . import views

urlpatterns = [
    path('', views.index),
    path('app/', views.application),
    path('app/store/', apps.get_store),
    path('app/product/', apps.get_item_from_name),
    path('app/price/',apps.get_price_location)
]