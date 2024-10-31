from django.urls import path

from apps.views import SendCodeAPIView, VerifyCodeAPIView, UserAPIView, CategoryRetrieveUpdateDestroyAPIView, \
    RestaurantRetrieveUpdateDestroyAPIView, \
    RestaurantCategoryRetrieveUpdateDestroyAPIView, ProductRetrieveUpdateDestroyAPIViewAPIView, \
    CategoryListCreateAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('send-email', SendCodeAPIView.as_view(), name='send_email'),
    path('verify-code', VerifyCodeAPIView.as_view(), name='verify_code'),
    path('user', UserAPIView.as_view(), name='user_list'),
    path('head-category', CategoryListCreateAPIView.as_view(), name='category'),
    path('head-category/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category'),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyAPIViewAPIView.as_view(), name='product'),
    path('restaurant/<int:pk>/', RestaurantRetrieveUpdateDestroyAPIView.as_view(), name='restaurant'),
    path('restaurant-category/<int:pk>/', RestaurantCategoryRetrieveUpdateDestroyAPIView.as_view(),
         name='restaurant_category'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
