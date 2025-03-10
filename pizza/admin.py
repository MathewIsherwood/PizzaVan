from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import pizza, order, order_item, payment

# Register your models here.
@admin.register(order)
class orderAdmin(SummernoteModelAdmin):
    """
    This class is used to configure the about app.
    **Context**
    """
    summernote_fields = ('ID', 'UserID', 'Order_date', 'Status', 'Total_price','Forward_order','Forward_order_time')
    
  
"""@admin.register(pizza)
class CollaborateRequestAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)

@admin.register(order_item)
class CollaborateRequestAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)

@admin.register(payment)
class CollaborateRequestAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)
"""