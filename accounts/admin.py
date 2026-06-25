from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    # This adds your custom fields (DOB, Goal) to the Admin Edit page
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Profile Info', {'fields': ('date_of_birth', 'financial_goal')}),
    )
    # This shows the fields in the list view
    list_display = ['username', 'email', 'date_of_birth', 'financial_goal', 'is_staff']

admin.site.register(User, CustomUserAdmin)