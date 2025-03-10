from django.db import models

# Create your models here.

class order(models.Model):
    """
    Stores a single order related to  :model:`auth.User`.
    """
    
    ID = models.IntegerField(primary_key=True, auto_created=True)
    User_ID = models.ForeignKey("auth.User", verbose_name=("User_ID"), on_delete=models.CASCADE)
    Order_date = models.DateTimeField(auto_now_add=True)
    Status = models.CharField(max_length=9)
    Total_price = models.DecimalField(max_digits=10, decimal_places=2)
    Forward_order = models.BooleanField(default=False)
    Forward_order_time = models.DateTimeField(auto_now_add=False)

class pizza(models.Model):
    """
    stores a single pizza entry with the following fields:
    """
    ID = models.IntegerField(primary_key=True, auto_created=True)
    Name = models.CharField(max_length=100)
    Size = models.CharField(max_length=6)
    Price = models.DecimalField(max_digits=6, decimal_places=2)
    Description = models.TextField()
    
class order_item(models.Model):
    """ 
    Stores a single pizza order entry with the following fields:
    """
    ID = models.IntegerField(primary_key=True, auto_created=True)
    Order_ID = models.ForeignKey(order, verbose_name=("Order_ID"), on_delete=models.CASCADE)
    Pizza_ID = models.IntegerField(models.ForeignKey("app.Model", verbose_name=("Pizza_ID"), on_delete=models.CASCADE))
    Quantity = models.IntegerField()
    
class payment(models.Model):
    """
    Stores a single payment entry with the following fields:
    """
    ID = models.IntegerField(primary_key=True, auto_created=True)
    Order_ID = models.ForeignKey(order, verbose_name=("Order_ID"), on_delete=models.CASCADE)
    Payment_method = models.CharField(max_length=12)
    Payment_status = models.CharField(max_length=8)
    Transaction_ID = models.IntegerField(auto_created=True)
    
