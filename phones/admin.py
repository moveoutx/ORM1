from django.contrib import admin

# Register your models here.
from .models import Phone


class PhoneAdmin(admin.ModelAdmin):
    repopulated_fields = {"slug": ("name",)}


admin.site.register(Phone, PhoneAdmin)
