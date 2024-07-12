from django.contrib.admin import register, ModelAdmin, StackedInline

from apps.models import Product, ProductImage


@register(ProductImage)
class ProductImageModelAdmin(ModelAdmin):
    pass


class ProductImageInline(StackedInline):
    model = ProductImage
    extra = 1
    min_num = 1


@register(Product)
class ProductModelAdmin(ModelAdmin):
    inlines = [ProductImageInline]
