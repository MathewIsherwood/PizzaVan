from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Pizza

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