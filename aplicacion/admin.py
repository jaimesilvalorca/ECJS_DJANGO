from django.contrib import admin
from .models import Product, Cart, ItemCart, Order

    
class ProductAdmin(admin.ModelAdmin):
    list_display:('name','platform','description','price','quantity','image')

class CartAdmin(admin.ModelAdmin):
    list_display:('user','products')

class ItemCartAdmin(admin.ModelAdmin):
    list_display:('product','cart','quantity')

class OrderAdmin(admin.ModelAdmin):
    list_display:('user','order_number','total_price')
    
    
admin.site.register(Product,ProductAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(ItemCart,CartAdmin)
admin.site.register(Order,OrderAdmin)
