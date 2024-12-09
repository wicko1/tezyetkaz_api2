from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.views import SendCodeAPIView, VerifyCodeAPIView, UserAPIView, ProductRetrieveDestroyAPIViewAPIView, \
    CategoryListCreateAPIView, CategoryRetrieveDestroyAPIView, RestaurantListCreateAPIView, \
    RestaurantRetrieveDestroyAPIView, RestaurantCategoryListCreateAPIView, RestaurantCategoryRetrieveDestroyAPIView, \
    OrdersListAPIView, SearchFilterListAPIView

urlpatterns = [
    path('send-email', SendCodeAPIView.as_view(), name='send_email'),
    path('verify-code', VerifyCodeAPIView.as_view(), name='verify_code'),
    path('user', UserAPIView.as_view(), name='user_list'),
    path('head-category', CategoryListCreateAPIView.as_view(), name='category_list'),
    path('head-category/<int:pk>/', CategoryRetrieveDestroyAPIView.as_view(), name='category_detail'),
    path('product/<int:pk>', ProductRetrieveDestroyAPIViewAPIView.as_view(), name='product'),
    path('restaurant', RestaurantListCreateAPIView.as_view(), name='restaurant_list'),
    path('restaurant/<int:pk>/', RestaurantRetrieveDestroyAPIView.as_view(), name='restaurant_detail'),
    path('restaurant-category', RestaurantCategoryListCreateAPIView.as_view(), name='restaurant_category'),
    path('restaurant-category/<int:pk>/', RestaurantCategoryRetrieveDestroyAPIView.as_view(),
         name='restaurant_category_detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('order-list', OrdersListAPIView.as_view(), name='order_list'),
    path('search-filter', SearchFilterListAPIView.as_view(), name='search_filter'),

]
