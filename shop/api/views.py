from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from api.models import  CategoryModel,ProductModel
from api.serializers import CategorySerializersData,ProductSerializersData
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class PaginationView(PageNumberPagination):
    page_size=5
    page_query_param='page'
    max_page_size=8
    last_page_strings=['end','last']

class CategoryListView(ListCreateAPIView):
    queryset=CategoryModel.objects.all()
    serializer_class=CategorySerializersData
    pagination_class=PaginationView


class CategoryChangeView(RetrieveUpdateDestroyAPIView):
    queryset=CategoryModel.objects.all()
    serializer_class=CategorySerializersData

class ProductListView(ListCreateAPIView):
    queryset=ProductModel.objects.select_related('category').all()
    serializer_class=ProductSerializersData
    pagination_class=PaginationView

class ProductChangeView(RetrieveUpdateDestroyAPIView):
    queryset=ProductModel.objects.select_related('category').all()
    serializer_class=ProductSerializersData