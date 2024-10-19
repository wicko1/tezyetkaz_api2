from django.urls import path

from apps.views import SendCodeAPIView, VerifyCodeAPIView, UserAPIView, CategoryListCreateAPIView, ProductListAPIView

urlpatterns = [
    path('send-email', SendCodeAPIView.as_view(), name='send_email'),
    path('verify-code', VerifyCodeAPIView.as_view(), name='verify_code'),
    path('user', UserAPIView.as_view(), name='user-list'),
    path('category', CategoryListCreateAPIView.as_view(), name='user-list'),
    path('product', ProductListAPIView.as_view(), name='product-list'),
]
