from django.urls import path
from . import views


urlpatterns = [
    path("products", views.products, name="products"),
    path("product_detail/<slug:slug>", views.product_detail, name="product-detail"),
    path("add_item/", views.add_item, name="add_item"),
    path("products_in_cart/", views.products_in_cart, name="products_in_cart"),
    path('cart_status/', views.get_cart_status, name="cart_status"),
    path('get_cart/', views.get_cart, name="get_cart"),
    path("update_quantity/", views.update_quantity, name="update-quantity"),
    path("delete_cartitem/", views.delete_cartitem, name="delete_cartitem"),
    path("get_username/", views.get_username, name="get_username"),
    path("user_info/", views.user_info, name="user_info"),
    path("initiate_payment/", views.initiate_payment, name="initiate_payment"),
    path("payment_callback/", views.payment_callback, name="payment_callback"),
    path("initiate_paypal_payment/", views.initiate_paypal_payment, name="initiate_paypal_payment"),
    path("paypal_payment_callback/", views.paypal_payment_callback, name="paypal_payment_callback"),
    path("create_superuser_view/", views.create_superuser_view, name="create_superuser_view")
]