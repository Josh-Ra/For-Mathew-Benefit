from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import People


# Register your models here.
@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ("is_active", "name", "password")
    list_filter = ("is_active",)
    search_fields = ("name",)
