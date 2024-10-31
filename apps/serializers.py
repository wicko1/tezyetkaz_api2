from django.core.cache import cache
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import IntegerField, ModelSerializer
from rest_framework.serializers import Serializer, EmailField

from apps.models import Product, User, Category, Restaurant, RestaurantCategory






class SendCodeMailSerializer(Serializer):
    email = EmailField(
        max_length=255,
        help_text='olimcola@gmail.com'
    )

    def validate_email(self, value):
        if not value:
            raise ValidationError('Email is required')
        return value


class VerifyCodeSerializer(Serializer):
    email = EmailField(
        max_length=255,
        help_text='olimcola@gmail.com'
    )
    code = IntegerField(
        help_text='Enter the 4-digit code sent to your email'
    )

    def validate_email(self, value):
        if not value:
            raise ValidationError('Email is required')
        return value

    def validate(self, attrs):
        email = attrs.get('email')
        code = attrs.get('code')
        cache_code = cache.get(email)
        if code != cache_code:
            raise ValidationError('The code is incorrect or has expired!')
        return attrs


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'first_name', 'last_name',  'email', 'profile_photo'



class CategoryListModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = 'name', 'photo'


class CategoryDetailModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ()


class RestaurantListModelSerializer(ModelSerializer):
    categories = CategoryListModelSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        exclude = ('')




class RestaurantCategoryListModelSerializer(ModelSerializer):
    class Meta:
        model = RestaurantCategory
        exclude = ()


class ProductListModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ()

    def to_representation(self, instance: Product):
        repr = super().to_representation(instance)
        repr['category'] = CategoryListModelSerializer(instance.category).data
        return repr
