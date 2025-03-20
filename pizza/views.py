import datetime
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Pizza, Order, OrderItem, ContactUs
from .forms import ContactUsForm

# Create your views here.


class PizzaList(generic.ListView):
    queryset = Pizza.objects.filter(enabled=True)
    template_name = "pizza/order.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            today = timezone.now().date()
            cart_order = Order.objects.filter(user_id=self.request.user.id,
                                              status='Cart',
                                              order_date__date=today).first()
            if cart_order:
                order_items = cart_order.orderitem_set.filter(
                    order_id__order_date__date=today)
                context['order_items'] = order_items
            context['cart_order'] = cart_order
        return context


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
        # If an order exists, check if the pizza is already in the order
        order_item = existing_order.orderitem_set.filter(
            pizza_id=pizza).first()
        if order_item:
            # Increment the quantity if the pizza is already in the order
            order_item.quantity += 1
            order_item.save()
            messages.success(
                request,
                'The quantity of the pizza in your order '
                'has been updated successfully.'
            )
        else:
            # Add the pizza to the existing order
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
    today = timezone.now().date()
    order = Order.objects.filter(
        user_id=request.user,
        forward_order_time__date=today
    ).first()

    if not order:
        messages.error(request,
                       'No order on file, you haven\'t started your order yet.'
                       )
        return HttpResponseRedirect(reverse('order_url'))

    try:
        order_item_to_delete = OrderItem.objects.get(
            order_id=order,
            pizza_id=id
        )
    except OrderItem.DoesNotExist:
        messages.error(request,
                       'This pizza is not on your order to delete, '
                       'so you cannot delete it.'
                       )
        return HttpResponseRedirect(reverse('order_url'))

    if order.user_id == request.user:
        # Delete the specific OrderItem
        order_item_to_delete.delete()
        messages.success(request, 'Your pizza has been removed from '
                         'your basket successfully.')
    else:
        messages.error(request, 'You can only delete your own pizzas!')

    return HttpResponseRedirect(reverse('order_url'))


@login_required
def my_orders(request):
    orders = Order.objects.filter(
        user_id=request.user).order_by(
            '-forward_order_time')
    return render(request, 'pizza/my_orders.html', {'orders': orders})


@login_required
def update_pizza_quantity(request, item_id):
    if request.method == 'POST':
        today = timezone.now().date()
        order_item = get_object_or_404(
            OrderItem, id=item_id, order_id__user_id=request.user.id
        )

        # Check if the order is from today
        if order_item.order_id.order_date.date() != today:
            messages.error(request, 'You can only update orders from today.')
            return HttpResponseRedirect(reverse('order_url'))

        # Get the new quantity from the form
        quantity_input = request.POST.get(
            'quantity', '').strip()  # Get and strip the input
        if not quantity_input.isdigit() or int(quantity_input) <= 0:
            # Handle invalid or empty input
            messages.error(
                request,
                'Please enter a valid quantity greater than 0.'
                )
            return HttpResponseRedirect(reverse('order_url'))

        # Update the quantity if valid
        new_quantity = int(quantity_input)
        order_item.quantity = new_quantity
        order_item.save()
        messages.success(
            request,
            'The quantity has been updated successfully.'
            )

    return HttpResponseRedirect(reverse('order_url'))


def contact_us(request):
    if request.method == "POST":
        contactus_form = ContactUsForm(data=request.POST)
        if contactus_form.is_valid():
            contactus_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Thank you for your message. "
                                 "I endeavour to respond within "
                                 "2 working days.")

    contactus_form = ContactUsForm()

    return render(
        request,
        "pizza/contact_us.html",
        {"contactus_form": contactus_form},
    )
