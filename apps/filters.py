from unicodedata import category

from django_filters import FilterSet, CharFilter

from apps.models import Product, Restaurant




class ProductSearchFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name']
