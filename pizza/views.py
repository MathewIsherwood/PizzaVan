from django.shortcuts import render

# Create your views here.
def index(request):
    """
    **Template:**
    :template:`pizza/index.html`
    """
    return render(request, 'pizza/index.html')

