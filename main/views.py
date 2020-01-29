from django.shortcuts import render,redirect
from .models import Item,OrderItem,Order
# Create your views here.
def index(request):   
    context = {
        "items" : Item.objects.all(),
    }
    return render(request,"index.html",context)

def add_item(request):
    title = request.POST['title']
    desp = request.POST['description']
    price = request.POST['price']
    item = Item.objects.create(title = title,price = price, description = desp)
    
       
    return redirect('/item')

def home(request):   
    request.session['user'] = 'sun'
    orders = OrderItem.objects.filter(user = request.session['user'])
    context = {
        "items" : Item.objects.all(),
        "orders":orders
    }
    return render(request,"home.html",context)

def product(request,id):   
    context = {
        "item" : Item.objects.get(id = id),
    }
    return render(request,"product.html",context)

def add_to_cart(request,id):
    item = Item.objects.get(id = id)
    print(id)
    order_item = OrderItem.objects.filter(user = request.session['user'], item = item)
    if order_item.exists():
        order_item[0].quantity += 1
        order_item.save()
    else:
        OrderItem.objects.create(user = request.session['user'], item = item,quantity = 1)

    return redirect('/')

def summary(request):
    context = {
        "items" : OrderItem.objects.filter(user = request.session['user']),
    }
    return render(request,"summary.html",context)

# def remove_from_cart(request,id):
#     item = Item.objects.get(id = id)
#     order_item = OrderItem.objects.filter(user = request.session['user'], item = item)

