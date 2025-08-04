from django.urls import path
from api import views

urlpatterns = [
    path('category/', views.CategoryListView.as_view(),name='categorylist'),
    path('categorychange/<int:pk>', views.CategoryChangeView.as_view(),name='categorychange'),
    path('product/', views.ProductListView.as_view(),name='productlist'),
    path('productchange/<int:pk>', views.ProductChangeView.as_view(),name='categorychange'),

]