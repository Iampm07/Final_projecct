from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('product_name',)}

admin.site.register(models.Product,ProductAdmin)
admin.site.register(models.Variation)