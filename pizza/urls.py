from django.urls import path
from . import views

urlpatterns = [
    path('', views.PizzaList.as_view(),
         name='order_url'),
    path("order/<int:id>/",
         views.order_pizza,
         name='order_pizza'),
    path("my_orders/",
         views.my_orders,
         name='my_orders'),
    path("delete_order/<int:id>/",
         views.delete_pizza_order,
         name='delete_pizza_order'),
    path("update_pizza_quantity/<int:item_id>/", 
         views.update_pizza_quantity,
         name='update_pizza_quantity'),
    path('contact_us/',
         views.contact_us,
         name='contactus'),
]
