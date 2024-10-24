
from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Discount, Product, Comment, Category, Color

admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Discount)


class CommentInline(admin.TabularInline):
    model= Comment
    fields= ( 'author', 'stars', 'active', )
    extra= 0


@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin ,admin.ModelAdmin):
    list_display= ('title', 'price', 'active',)

    inlines= [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''Admin View for Comment'''

    list_display = ('product', 'author', 'stars', 'active', )
    list_filter = ('active',)
    readonly_fields = ('product',)
    search_fields = ('product', 'author',)

