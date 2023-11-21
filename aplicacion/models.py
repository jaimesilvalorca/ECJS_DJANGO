from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    platform = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    image = models.TextField(blank=True)
    
    def __str__(self):
        return self.name + ' ' + self.platform
    
    
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,through='ItemCart')
    
    def __str__(self):
        return f'Cart de {self.user.first_name}'
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    order_number = models.CharField(max_length=20,default=0, unique=False)
    total_price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Order {self.order_number} for {self.user.username}'
    
class ItemCart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,default=1)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f'{self.quantity} x {self.product.name} en {self.cart}'
    





    
