from django.urls import path
from .views import *

urlpatterns =[
    path('', main_dashboard, name="main_dashboard"),
    path('login/',login_page, name="login_page"),
    path('logout/', logout_page, name="logout_page"),

    path('category/list/', category_list, name="category_list"),
    path('category/create/', category_create, name="category_create"),
    path('category/<int:pk>/edit/', category_edit, name="category_edit"),
    path('category/<int:pk>/delete/',category_delete, name="category_delete"),

    path('product/list/', product_list, name="product_list"),
    path('product/create/', product_create, name="product_create"),
    path('product/<int:pk>/edit/', product_edit, name="product_edit"),
    path('product/<int:pk>/delete/',product_delete, name="product_delete"),

    # path('users/list/<int:pk>/', users_list, name="users_list_with_pk"),
    path('users/list/', users_list, name="users_list"),
    path('user/create/', user_create, name="user_create"),
    path('user/<int:pk>/edit/', user_edit, name="user_edit"),
    path('user/<int:pk>/delete/', user_delete, name="user_delete"),

    path('order/list/', order_list, name="order_list"),
    path('orderproduct/<int:pk>/list', orderproduct_list, name='orderproduct_list')

]