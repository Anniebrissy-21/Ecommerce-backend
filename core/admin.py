from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from shop_apps.models import Product, Cart, CartItem, Transaction

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','first_name','last_name','email', 'password1', 'password2', 'city', 'state', 'address',
                       'phone', 'is_staff', 'is_active'),}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Transaction)