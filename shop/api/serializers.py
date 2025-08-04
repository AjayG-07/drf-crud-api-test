from rest_framework import serializers
from api.models import CategoryModel,ProductModel

class CategorySerializersData(serializers.ModelSerializer):
    class  Meta:
        model=CategoryModel
        fields=['id','name']


class ProductSerializersData(serializers.ModelSerializer):
    category=CategorySerializersData(read_only=True)
    category_id=serializers.PrimaryKeyRelatedField(
        queryset=CategoryModel.objects.all(),source='category',write_only=True
    )

    class  Meta:
        model=ProductModel
        fields=['id','name','price','descriptions','category','category_id']