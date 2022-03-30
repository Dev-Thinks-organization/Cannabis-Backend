from ast import Mod
from rest_framework.serializers import ModelSerializer
from .models import Items, Category, Benefits  # type: ignore


class ItemsSerializer(ModelSerializer):
    class Meta:
        model = Items
        fields = "__all__"


class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class CategorySerializer(ModelSerializer):
    children = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ["name", "children"]


class CategoryAncestorSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class BenefitsSerializer(ModelSerializer):
    class Meta:
        model = Benefits
        fields = "__all__"
