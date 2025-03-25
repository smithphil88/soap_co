from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, Ingredient, ProductGallery


class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 3

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
        'is_bundle',
        'image',
        'weight',
    )

    list_filter = ('category', 'is_bundle')
    ordering = ('name',)
    filter_horizontal = ('ingredients',)

    inlines = [ProductGalleryInline]

    def get_fields(self, request, obj=None):
        """ Show bundle_items field only if the product is a bundle """
        fields = [
            'name', 'category', 'price', 'is_bundle', 'image', 'weight',
            'description']
        if obj and obj.is_bundle:
            fields.append('bundle_items')
        return fields

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        """ Restrict bundle_items to non-bundle products only """
        if db_field.name == "bundle_items":
            kwargs["queryset"] = Product.objects.filter(is_bundle=False)
        return super().formfield_for_manytomany(db_field, request, **kwargs)


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
