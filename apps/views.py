from itertools import product
from random import randint

from django.core.cache import cache
from django.core.mail import send_mail
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, \
    RetrieveDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.filters import ProductSearchFilter
from apps.models import Product, User, Category, Restaurant, RestaurantCategory
from apps.serializers import (
    SendCodeMailSerializer,
    VerifyCodeSerializer, ProductListModelSerializer, UserModelSerializer, CategoryListModelSerializer,
    RestaurantListModelSerializer, RestaurantCategoryListModelSerializer, CategoryDetailModelSerializer,
    RestaurantDetailModelSerializer, RestaurantCategoryDetailModelSerializer, OrdersListModelSerializer,
    SearchModelSerializer,
)


@extend_schema(tags=['User'])
class UserAPIView(ListAPIView):
    queryset = User.objects.order_by('id')
    serializer_class = UserModelSerializer
    permission_classes = AllowAny,


@extend_schema(tags=['auth'])
class SendCodeAPIView(GenericAPIView):
    serializer_class = SendCodeMailSerializer
    permission_classes = AllowAny,

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
    permission_classes = AllowAny,

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"message": "OK"}, status=status.HTTP_200_OK)


@extend_schema(tags=['head_category'])
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.order_by('id')
    serializer_class = CategoryListModelSerializer
    permission_classes = AllowAny,


@extend_schema(tags=['head_category'])
class CategoryRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailModelSerializer
    permission_classes = AllowAny,


@extend_schema(tags=['restaurant'])
class RestaurantListCreateAPIView(ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListModelSerializer
    permission_classes = AllowAny,


@extend_schema(tags=['restaurant'])
class RestaurantRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantDetailModelSerializer
    permission_classes = AllowAny,


@extend_schema(tags=['restaurant_category'])
class RestaurantCategoryListCreateAPIView(ListCreateAPIView):
    queryset = RestaurantCategory.objects.all()
    serializer_class = RestaurantCategoryListModelSerializer
    permission_classes = AllowAny,


@extend_schema(tags=['restaurant_category'])
class RestaurantCategoryRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = RestaurantCategory.objects.all()
    serializer_class = RestaurantCategoryDetailModelSerializer
    permission_classes = AllowAny,


@extend_schema(tags=['product'])
class ProductRetrieveUpdateDestroyAPIViewAPIView(RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListModelSerializer
    permission_classes = AllowAny,


@extend_schema(tags=['Order_product'])
class OrdersListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = OrdersListModelSerializer


@extend_schema(tags=['Search_Filter'])
class SearchFilterListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = SearchModelSerializer
    filterset_class = ProductSearchFilter
    permission_classes = AllowAny,