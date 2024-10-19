from django.contrib import admin
from django.utils.html import format_html
from mptt.admin import DraggableMPTTAdmin
from .models import User, Category, Restaurant, RestaurantCategory, Product


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email' , 'profile_image', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    ordering = ('id',)

    def profile_image(self, obj):
        if obj.profile_photo:
            return format_html(
                f'<img src="{obj.profile_photo.url}" width="50" height="50" style="border-radius: 50%;" />')
        return 'No Image'

    profile_image.short_description = 'Profile Photo'


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'photo_preview', 'parent')
    list_display_links = ('indented_title',)
    search_fields = ('name',)

    def photo_preview(self, obj):
        if obj.photo:
            return format_html(f'<img src="{obj.photo.url}" width="50" height="50" />')
        return 'No Image'

    photo_preview.short_description = 'Photo'


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'logo_preview', 'work_start_time', 'work_end_time', 'service_price')
    search_fields = ('name',)
    list_filter = ('category',)
    ordering = ('id',)

    def logo_preview(self, obj):
        if obj.logo:
            return format_html(f'<img src="{obj.logo.url}" width="50" height="50" />')
        return 'No Logo'

    logo_preview.short_description = 'Logo'


@admin.register(RestaurantCategory)
class RestaurantCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'restaurant')
    search_fields = ('name', 'restaurant__name')
    list_filter = ('restaurant',)
    ordering = ('id',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'image_preview')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    ordering = ('id',)

    def image_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="50" height="50" />')
        return 'No Image'

    image_preview.short_description = 'Image'