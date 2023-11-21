from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db import IntegrityError
from django.utils import timezone
from django.http import JsonResponse
from .forms import UserForm,ProductForm
from .models import Cart,Product,ItemCart,Order
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages

def index(request):
    return render(request,'products/index.html')

def products(request):
    products = Product.objects.all()

    return render(request,'products/products.html',{
        'products':products
    })
    
def productDetail(request,product_id):
    if request.method == 'GET':
        product = get_object_or_404(Product,pk=product_id)
        return render(request,'products/productdetail.html',{
            'product':product
        })

def form(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('emailAddress')
        message = request.POST.get('message')

        subject = 'Nuevo mensaje de contacto'
        message_content = f'Nombre: {name}\nCorreo Electrónico: {email}\nMensaje: {message}'

        send_mail(
            subject,
            message_content,
            'jaimesilvalorca@gmail.com', 
            ['jaimesilvalorca@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'user/contacto.html',{
            'message':'Mensaje enviado correctamente'
        })

    return render(request, 'user/contacto.html')

def userForm(request):
    if request.method == 'GET':
        return render(request,'user/register.html',{
            'form':UserForm,
        })
    else:
        user = UserForm(request.POST)
        new_user = user.save(commit=False)
        new_user.save()
        login(request,new_user)
        nuevo_carrito = Cart.objects.create(user=new_user)
        return redirect('products')

def addToCart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    item_cart, item_created = ItemCart.objects.get_or_create(product=product, cart=cart)
    
    if not item_created:
        item_cart.quantity += 1
        item_cart.save()
    
    return redirect('products')

def viewCart(request):
    cart = Cart.objects.get(user=request.user)
    items = ItemCart.objects.filter(cart=cart)

    products_info = []
    total_price = 0

    for item in items:
        product_info = {
            'name': item.product.name,
            'price': item.product.price,
            'quantity_in_cart': item.quantity,
        }
        product_info['total'] = product_info['price'] * product_info['quantity_in_cart']
        total_price += product_info['total']
        products_info.append(product_info)

    return render(request, 'cart/view_cart.html', {'cart': cart, 'products_info': products_info, 'total_price': total_price})
    

def productForm(request):
    if request.method == 'GET':
        return render(request,'administrator/product.html',{
            'form':ProductForm
        })
    else:
        product = ProductForm(request.POST)
        new_product = product.save(commit=False)
        new_product.save()
        return render(request,'administrator/product.html',{
            'form':ProductForm,
            'message':'Producto agregado correctamente'
        })
    
def signin(request):
    if request.method == 'GET':
        return render(request,'user/signin.html',{
            'form':AuthenticationForm
        })
    else:
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password']
                            )
        if user is None:
            return render(request,'user/signin.html',{
                'form':AuthenticationForm,
                'error':'Username or password is incorrect'
            })
        else:
            login(request,user)
            return (redirect('products'))
        
def signout(request):
    logout(request)
    return redirect('index')

def checkout(request):
   
    cart = Cart.objects.get(user=request.user)
    order_number = timezone.now().strftime('%Y%m%d%H%M%S')
    order = Order.objects.create(user=request.user, order_number=order_number, total_price=0)
    products_in_cart = cart.products.all()
    total_price = 0
    for product_in_cart in products_in_cart:
        ItemCart.objects.create(product=product_in_cart, cart=cart, order=order, quantity=product_in_cart.quantity)
        total_price += product_in_cart.price * product_in_cart.quantity

    order.total_price = total_price
    order.save()
    send_order_email(order)
    cart.products.clear()

    return render(request, 'order/checkout_success.html', {'order': order})

def send_order_email(order):
    subject = f'Confirmación de pedido #{order.order_number}'
    html_message = render_to_string('order/order_confirmation_email.html', {'order': order})
    plain_message = strip_tags(html_message)
    from_email = 'jaimesilvalorca@gmail.com'
    to_email = [order.user.email]

    send_mail(subject, plain_message, from_email, to_email, html_message=html_message)