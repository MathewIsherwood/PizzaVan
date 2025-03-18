from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

# MoSCoW Prioritization - Must Have


class Order(models.Model):
    """
    Stores a single order related to  :model:`auth.User`.
    """
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        "auth.User",
        verbose_name=("User_ID"),
        on_delete=models.CASCADE
        )
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=9,
        choices=[('Cart', 'Cart'),
                 ('Pending', 'Pending'),
                 ('Prepared', 'Prepared'),
                 ('Delivered', 'Delivered'),
                 ('Cancelled', 'Cancelled')]
        )
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    forward_order = models.BooleanField(
        default=False,
        choices=[(True, 'Yes'),
                 (False, 'No')]
        )
    forward_order_time = models.DateTimeField(auto_now_add=False)


class Pizza(models.Model):
    """
    stores a single pizza entry with the following fields:
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    size = models.CharField(
        max_length=6,
        choices=[('Small', 'Small'),
                 ('Medium', 'Medium'),
                 ('Large', 'Large')]
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    enabled = models.BooleanField(
        default=False,
        choices=[(
            True, 'Yes'),
            (False, 'No')]
        )


class OrderItem(models.Model):
    """
    Stores the reference to the order and the
    pizza with the quantity ordered with the following fields:
    """
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(
        Order,
        verbose_name=("Order_ID"),
        on_delete=models.CASCADE
        )
    pizza_id = models.ForeignKey(
        Pizza,
        verbose_name=("Pizza_ID"),
        on_delete=models.CASCADE
        )
    quantity = models.PositiveIntegerField()


# MoSCoW Prioritization - Should Have
class Payment(models.Model):
    """
    Stores a single payment entry with the following fields:
    """
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(
        Order,
        verbose_name=("Order_ID"),
        on_delete=models.CASCADE
        )
    payment_method = models.CharField(
        max_length=12,
        choices=[('Credit Card', 'Credit Card'),
                 ('PayPal', 'PayPal'),
                 ('Cash', 'Cash')]
        )
    payment_status = models.CharField(
        max_length=8,
        choices=[('Paid', 'Paid'),
                 ('Pending', 'Pending'),
                 ('Failed', 'Failed')]
        )


class ContactUs(models.Model):
    """
    Stores a single contact request entry.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact Us from {self.name}"
