import datetime
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Pizza, Order, OrderItem

# Create your views here.


class PizzaList(generic.ListView):
    queryset = Pizza.objects.filter(enabled=True)
    template_name = "pizza/order.html"
    paginate_by = 12


def index(request):
    """
    **Template:**
    :template:`pizza/index.html`
    """
    return render(request, 'pizza/index.html')


def order(request):
    """
    **Template:**
    :template:`pizza/order.html`
    """
    return render(request, 'pizza/order.html')


@login_required
def order_pizza(request, id):
    pizza = get_object_or_404(Pizza, id=id)

    # Check if an order has already been opened today
    today = timezone.now().date()
    existing_order = Order.objects.filter(
        user_id=request.user,
        forward_order_time__date=today).first()

    if existing_order:
        # If an order exists, add the pizza to the existing order
        OrderItem.objects.create(
            order_id=existing_order,
            pizza_id=pizza,
            quantity=1
            )
        messages.success(
            request,
            'Your item has been added to your existing order successfully.'
            )
    else:
        # Create a new order
        order = Order.objects.create(
            user_id=request.user,
            total_price=pizza.price,
            status='Cart',
            forward_order_time=timezone.now()
            )
        OrderItem.objects.create(
            order_id=order,
            pizza_id=pizza,
            quantity=1
            )
        messages.success(
            request,
            'Your item has been added to your basket successfully.'
            )

    return HttpResponseRedirect(reverse('order_url'))


@login_required
def delete_pizza_order(request, id):
    order = Order.objects.get(
        user_id=request.user
        )
    order_item_to_delete = get_object_or_404(
        OrderItem,
        order_id=order,
        pizza_id=id
        )

    if order.user_id == request.user:
        # Delete the specific OrderItem
        order_item_to_delete.delete()
        messages.success(
            request,
            'Your pizza has been removed from your basket successfully.'
            )
    else:
        messages.error(request, 'You can only delete your own pizzas!')

    return HttpResponseRedirect(reverse('order_url'))


@login_required
def my_orders(request):
    orders = Order.objects.filter(
        user_id=request.user).order_by(
            '-forward_order_time')
    return render(request, 'pizza/my_orders.html', {'orders': orders})
