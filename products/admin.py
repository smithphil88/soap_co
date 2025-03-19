from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, Ingredient, ProductGallery

# Register your models here.


class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 3  # Allows adding 3 extra images per product

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" />', obj.image.url)
        return "No Image"

    image_preview.allow_tags = True
    image_preview.short_description = "Image Preview"


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'image',
        'weight',
    )

    inlines = [ProductGalleryInline]
    ordering = ('name',)
    filter_horizontal = ('ingredients',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="50" height="50" />'
        return "No Image"

    image_preview.allow_tags = True
    image_preview.short_description = "Image Preview"


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductGallery)
