from django.core.cache import cache
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import IntegerField, ModelSerializer
from rest_framework.serializers import Serializer, EmailField

from apps.models import Product, User, Category, Restaurant, RestaurantCategory


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


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


class CategoryListModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class RestaurantListModelSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        exclude = ('category',)


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
        repr['user'] = UserModelSerializer(instance.name).data
        repr['category'] = CategoryListModelSerializer(instance.category).data
        return repr