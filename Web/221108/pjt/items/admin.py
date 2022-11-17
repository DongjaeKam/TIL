from django.contrib import admin
from .models import Item

# Register your models here.

# Register your models here.
class ItemrAdmin(admin.ModelAdmin):
    list_display=()
    fields =()

admin.site.register(Item)