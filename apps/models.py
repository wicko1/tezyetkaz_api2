from django.contrib.auth.models import AbstractUser
from django.db.models import (
    Model, CharField, ImageField, TimeField, IntegerField, ForeignKey, CASCADE, EmailField
)
from django_ckeditor_5.fields import CKEditor5Field
from mptt.models import MPTTModel, TreeForeignKey


class User(AbstractUser):
    first_name = CharField(max_length=255, null=True, blank=True)
    last_name = CharField(max_length=255, null=True, blank=True)
    profile_photo = ImageField(upload_to='profile_images/')


class Category(MPTTModel):
    name = CharField(max_length=255)
    photo = ImageField(upload_to='category_images/')
    parent = TreeForeignKey(
        'self', on_delete=CASCADE, null=True, blank=True, related_name='children'
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Restaurant(Model):
    name = CharField(max_length=255)
    logo = ImageField(upload_to='logos/')
    photo = ImageField(upload_to='restaurant_images/')
    work_start_time = TimeField()
    work_end_time = TimeField()
    category = ForeignKey(
        'apps.Category', on_delete=CASCADE, related_name='restaurants', null=True, blank=True
    )
    service_price = IntegerField()

    def __str__(self):
        return self.name


class RestaurantCategory(Model):
    name = CharField(max_length=255)  # max_length qo‘shildi
    restaurant = ForeignKey(
        'apps.Restaurant', on_delete=CASCADE, related_name='restaurant_categories', null=True, blank=True
    )

    def __str__(self):
        return f"{self.name} - {self.restaurant.name}"


class Product(Model):
    name = CharField(max_length=255)
    description = CKEditor5Field()
    image = ImageField(upload_to='product_images/')
    price = IntegerField()
    category = ForeignKey(
        'apps.Category', on_delete=CASCADE, related_name='products', null=True, blank=True
    )

    def __str__(self):
        return self.name