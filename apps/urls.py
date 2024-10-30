from django.urls import path

from apps.views import SendCodeAPIView, VerifyCodeAPIView, UserAPIView, ProductListAPIView, \
    CategoryRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('send-email', SendCodeAPIView.as_view(), name='send_email'),
    path('verify-code', VerifyCodeAPIView.as_view(), name='verify_code'),
    path('user', UserAPIView.as_view(), name='user-list'),
    path('head_category', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category'),
    path('product', ProductListAPIView.as_view(), name='product'),
    path('restaurant', ProductListAPIView.as_view(), name='restaurant'),
]
