from django.contrib import admin
from .models import UserPreference
# Register your models here.
@admin.register(UserPreference)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id','preferred_categories']