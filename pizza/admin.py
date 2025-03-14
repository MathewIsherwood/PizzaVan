from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Pizza, Order, OrderItem, Payment
from django import forms

# Register your models here.

# MoSCoW Prioritization - Must Have


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    This class is used to configure the Order model in the admin interface.
    """
    list_display = (
        'id',
        'user_id',
        'status',
        'total_price',
        'forward_order',
        'forward_order_time',
        )


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'size',
        'price',
        'description',
        'featured_image',
        'enabled',
        )
    list_filter = (
        'name',
        'size',
        'enabled',
        )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'order_id',
        'pizza_id',
        'quantity',
        )


# MoSCoW Prioritization - Should Have
class PaymentAdminForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('payment_method', 'payment_status')
        widgets = {
            'payment_method': forms.Select(choices=[
                ('Credit Card', 'Credit Card'),
                ('PayPal', 'PayPal'),
                ('Cash', 'Cash'),
            ]),
            'payment_status': forms.Select(choices=[
                ('Paid', 'Paid'),
                ('Pending', 'Pending'),
                ('Failed', 'Failed'),
            ]),
        }

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    form = PaymentAdminForm
    list_display = ('payment_method', 'payment_status')
    list_filter = ('payment_method',)
