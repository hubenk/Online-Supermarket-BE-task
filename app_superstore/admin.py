from django.contrib import admin
from django.utils.html import format_html

from app_superstore.models import UserProfile, Product


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'category', 'quantity', 'display_similar_products')
    exclude = ('similar_products',)
    readonly_fields = ('display_similar_products',)

    def display_similar_products(self, obj):
        similar_products = obj.get_similar_products()
        if not similar_products:
            return "No similar products"

        product_links = [
            f'<a href="/admin/app_superstore/product/{p.id}/change/">{p.product}</a>'
            for p in similar_products
        ]
        return format_html(", ".join(product_links))

    display_similar_products.short_description = "Similar Products"
