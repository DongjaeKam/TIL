from django.contrib import admin
from .models import Article

# Register your models here.
class ArticlerAdmin(admin.ModelAdmin):
    list_display=()
    fields =()

admin.site.register(Article)