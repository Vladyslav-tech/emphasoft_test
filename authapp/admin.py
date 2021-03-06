from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomerUserRegisterForm, CustomerUserEditForm
from .models import CustomerUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomerUserRegisterForm
    form = CustomerUserEditForm
    model = CustomerUser
    list_display = ['username', 'first_name', 'last_name', 'patronymic', 'email']

admin.site.register(CustomerUser, CustomUserAdmin)
