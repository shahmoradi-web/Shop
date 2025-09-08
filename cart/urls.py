from django.urls import path
from . import views

from .models import *

app_name='cart'
urlpatterns = [
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

]