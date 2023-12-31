from django.contrib import admin

# Register your models here.
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')
    list_filter = ('email', 'country')
