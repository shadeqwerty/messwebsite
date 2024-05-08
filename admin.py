from django.contrib import admin
from .models import MenuItem
from .models import FoodItem

admin.site.register(FoodItem)
admin.site.register(MenuItem)