from django.contrib import admin
from .models import Items, Size, Pizza

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Items)
admin.site.register(Size)