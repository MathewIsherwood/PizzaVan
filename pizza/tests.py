from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Order, OrderItem, Pizza
from django.utils import timezone


class PizzaAppTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.client = Client()

        # Create a test pizza
        self.pizza = Pizza.objects.create(
            name='Margherita',
            size='Medium',
            price=9.99,
            description='Classic Margherita Pizza',
            enabled=True
        )

        # Create a test order
        self.order = Order.objects.create(
            user_id=self.user,
            status='Cart',
            total_price=0,
            forward_order=False,
            forward_order_time=timezone.now()
        )

        # Create a test order item
        self.order_item = OrderItem.objects.create(
            order_id=self.order,
            pizza_id=self.pizza,
            quantity=1
        )

    def test_update_pizza_quantity_valid(self):
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        # Update the quantity of the pizza
        response = self.client.post(
            reverse('update_pizza_quantity', args=[self.order_item.id]),
            {'quantity': 2}
        )

        # Refresh the order item from the database
        self.order_item.refresh_from_db()

        # Assert the quantity was updated
        self.assertEqual(self.order_item.quantity, 2)
        self.assertRedirects(response, reverse('order_url'))

    def test_update_pizza_quantity_invalid(self):
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        # Try to update the quantity with an invalid value
        response = self.client.post(
            reverse('update_pizza_quantity', args=[self.order_item.id]),
            {'quantity': 0}
        )

        # Refresh the order item from the database
        self.order_item.refresh_from_db()

        # Assert the quantity was not updated
        self.assertEqual(self.order_item.quantity, 1)
        self.assertRedirects(response, reverse('order_url'))

    def test_update_pizza_quantity_empty(self):
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        # Try to update the quantity with an empty value
        response = self.client.post(
            reverse('update_pizza_quantity', args=[self.order_item.id]),
            {'quantity': ''}
        )

        # Refresh the order item from the database
        self.order_item.refresh_from_db()

        # Assert the quantity was not updated
        self.assertEqual(self.order_item.quantity, 1)
        self.assertRedirects(response, reverse('order_url'))

    def test_update_pizza_quantity_unauthenticated(self):
        # Try to update the quantity without logging in
        response = self.client.post(
            reverse('update_pizza_quantity', args=[self.order_item.id]),
            {'quantity': 2}
        )

        # Assert the user is redirected to the login page
        self.assertRedirects(
            response, f"{reverse('account_login')}?next={reverse(
                'update_pizza_quantity', args=[self.order_item.id])}")

    def test_order_button_visibility_authenticated(self):
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        # Get the order page
        response = self.client.get(reverse('order_url'))

        # Assert the order button is visible for pizzas not in the cart
        self.assertContains(response, f'id="OrderButton{self.pizza.id}"')

    def test_order_button_visibility_unauthenticated(self):
        # Get the order page without logging in
        response = self.client.get(reverse('order_url'))

        # Assert the user is prompted to log in
        self.assertContains(
            response,
            'Please <a href="/accounts/login/">login</a> to order pizza'
            )
