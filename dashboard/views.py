
from django.shortcuts import render, redirect, get_object_or_404
from food.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from . import forms
from . import services
from .forms import ProductForm


def login_required_decorator(func):
    return login_required(func, login_url='login_page')

@login_required_decorator
def main_dashboard(request):
    categories =Category.objects.all()
    products=Product.objects.all()
    customers=Customer.objects.all()
    orders=Order.objects.all()
    categories_products = []
    table_list =services.get_table()
    recent_orders_list=services.get_recent_orders()
    print(recent_orders_list)
    for category in categories:
        categories_products.append(
            {
                "category":category.title,
                "product":len(Product.objects.filter(category_id=category.id))
            }
        )

    ctx = {
        "counts":{
            "categories": len(categories),
            "products": len(products),
            "customers":len(customers),
            "orders":len(orders),
        },
        "categories_products": categories_products,
        "table_list":table_list,
        "recent_orders_list": recent_orders_list
    }
    return render(request, 'dashboard/index.html', ctx)


def login_page(request):
    if request.POST:
        username=request.POST.get("username", None)
        password=request.POST.get("password", None)
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_dashboard')
    return render(request, 'dashboard/register/login.html')


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect('login_page')

@login_required_decorator
def category_list(request):
    categories=Category.objects.all()

    ctx= {
        'categories': categories,


    }
    return render(request, "dashboard/category/list.html", ctx)

@login_required_decorator
def category_create(request):
    model= Category()
    form= forms.CategoryForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('category_list')
    ctx={
        'model':model,
        'form': form,
    }
    return render(request, 'dashboard/category/form.html', ctx)

@login_required_decorator
def category_edit(request, pk):
    model=Category.objects.get(pk=pk)
    form=forms.CategoryForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('category_list')
    ctx={
        'model': model,
        'form': form,
        'edit':'edit',


    }
    return render(request, 'dashboard/category/form.html', ctx)


@login_required_decorator
def category_delete(request, pk):
    model=Category.objects.get(pk=pk)
    model.delete()
    return redirect('category_list')

# Product

@login_required_decorator
def product_list(request):
    products = Product.objects.all()

    ctx ={
        'products': products
    }
    return render(request, 'dashboard/product/list.html', ctx)


@login_required_decorator
def product_create(request):
    model = Product()
    form = forms.ProductForm(request.POST or None, request.FILES, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('product_list')

    ctx= {
        'model':model,
        'form':form,
    }
    return render(request, 'dashboard/product/form.html', ctx)


@login_required_decorator
def product_edit(request, pk):
    model= Product.objects.get(pk=pk)
    form = ProductForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('product_list')

    ctx={
        'model': model,
        'form': form,
        'edit':'edit',
    }
    return render(request, 'dashboard/product/form.html', ctx)


@login_required_decorator
def product_delete(request, pk):
    model=Product.objects.get(pk=pk)
    model.delete()
    return redirect('product_list')

# User Form
@login_required_decorator
def users_list(request):
    users=Customer.objects.all()
    ctx={
        'users':users,
        "show_modal": True
    }


    return render(request, 'dashboard/users/user-list.html', ctx)


@login_required_decorator
def user_create(request):
    model=Customer()
    form=forms.UserForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('users_list')
    ctx= {
        'model':model,
        'form':form,
    }
    return render(request, 'dashboard/users/form.html',ctx)


@login_required_decorator
def user_edit(request, pk):
    customer_orders = services.get_order_by_user(id=pk)
    model = Customer.objects.get(pk=pk)
    form = forms.UserForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('users_list')
    ctx={
        'model':model,
        'form':form,
        'customer_orders':customer_orders,
    }
    return render(request, 'dashboard/users/user_edit.html', ctx)


@login_required_decorator
def user_delete(request, pk):
    model=Customer.objects.get(pk=pk)
    model.delete()
    return redirect('users_list')

# Order list
@login_required_decorator
def order_list(request):
    orders = Order.objects.all()
    ctx ={
        'orders': orders,

    }
    return render(request, "dashboard/orders/list.html", ctx)


@login_required_decorator
def orderproduct_list(request, pk):
    orderproduct_list=services.get_product_by_order(id=pk)
    customer= services.get_user_by_order(id=pk)
    print(orderproduct_list)

    ctx= {
        'orderproduct_list':orderproduct_list,
        'customer': customer,
    }

    return render(request, 'dashboard/orderproduct/user_view.html', ctx)

