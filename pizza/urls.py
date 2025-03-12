from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("order/", views.PizzaList.as_view(), name='order_url'),
]