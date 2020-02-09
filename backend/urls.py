from django.urls import path

from . import apps
from . import views

urlpatterns = [
    path('', views.index),
    path('app/', views.application),
    path('app/store/', apps.get_store),
    path('app/price/', apps.get_price_location_image),
    path('app/products/', apps.get_products_list),
    path('app/spf/',apps.get_spf)
]