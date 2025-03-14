from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("order/", views.PizzaList.as_view(), name='order_url'),
    path(
        "order/<int:id>/",
        views.order_pizza,
        name='order_pizza'
    ),
    path("delete_order/<int:id>/",
         views.delete_pizza_order,
         name='delete_pizza_order'
         ),
    path("my_orders/",
         views.my_orders,
         name='my_orders'
         ),
]
