# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Account
from .forms import UserCreationForm, UserChangeForm


class AccountAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'username','is_staff','is_superuser','is_vip','is_nonvip')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('email','username','is_staff', 'is_superuser','is_vip','is_nonvip','password')}),
        ('Personal info', {'fields': ('first_name','last_name','phone')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email','username','is_staff', 'is_superuser','is_vip','is_nonvip','password1', 'password2')}),
        ('Personal info', {'fields': ('first_name','last_name','phone',)}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('email', 'username', 'phone')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(Account, AccountAdmin)
