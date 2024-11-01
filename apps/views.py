from random import randint

from django.core.cache import cache
from django.core.mail import send_mail
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, \
    RetrieveDestroyAPIView
from rest_framework.response import Response

from apps.models import Product, User, Category, Restaurant, RestaurantCategory
from apps.serializers import (
    SendCodeMailSerializer,
    VerifyCodeSerializer, ProductListModelSerializer, UserModelSerializer, CategoryListModelSerializer,
    RestaurantListModelSerializer, RestaurantCategoryListModelSerializer, CategoryDetailModelSerializer,
    RestaurantDetailModelSerializer, RestaurantCategoryDetailModelSerializer,
)


@extend_schema(tags=['User'])
class UserAPIView(ListAPIView):
    queryset = User.objects.order_by('id')
    serializer_class = UserModelSerializer


@extend_schema(tags=['auth'])
class SendCodeAPIView(GenericAPIView):
    serializer_class = SendCodeMailSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        code = randint(1000, 9999)
        cache.set(email, code, timeout=120)
        print(f"Email: {email}, Code: {code}")
        send_mail(
            'Your Verification Code',
            f'Your verification code is {code}',
            'asadbekmehmonjonov5@gmail.com',
            [email],
            fail_silently=False,
        )
        return Response({"message": "Code sent successfully"}, status=status.HTTP_200_OK)


@extend_schema(tags=['auth'])
class VerifyCodeAPIView(GenericAPIView):
    serializer_class = VerifyCodeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"message": "OK"}, status=status.HTTP_200_OK)


@extend_schema(tags=['head_category'])
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.order_by('id')
    serializer_class = CategoryListModelSerializer


@extend_schema(tags=['head_category'])
class CategoryRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailModelSerializer


@extend_schema(tags=['restaurant'])
class RestaurantListCreateAPIView(ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListModelSerializer


@extend_schema(tags=['restaurant'])
class RestaurantRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantDetailModelSerializer


@extend_schema(tags=['restaurant_category'])
class RestaurantCategoryListCreateAPIView(ListCreateAPIView):
    queryset = RestaurantCategory.objects.all()
    serializer_class = RestaurantCategoryListModelSerializer


@extend_schema(tags=['restaurant_category'])
class RestaurantCategoryRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = RestaurantCategory.objects.all()
    serializer_class = RestaurantCategoryDetailModelSerializer


@extend_schema(tags=['product'])
class ProductRetrieveUpdateDestroyAPIViewAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListModelSerializer
