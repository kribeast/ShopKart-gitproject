from django.contrib import admin
from products.models import *
from django.utils.html import format_html

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    # def thumbnail(self, object):
    #     return format_html('<img src="{}" width="70px" style="border-radius: 40px;"/>'.format(object.category_image.url))

    # thumbnail.short_description = 'Images'

    list_display=['category_name', 'slug',]

admin.site.register(Category, CategoryAdmin)


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'slug','price']
    readonly_fields = ['created_at','updated_at']
    inlines=[ProductImageAdmin]

@admin.register(SizeVarient)
class SizeVarientAdmin(admin.ModelAdmin):
    list_display = ['size_name','price']
    model = SizeVarient

admin.site.register(Product ,ProductAdmin)

admin.site.register(ProductImage)
