from django.shortcuts import render
from items.serializers import (
    CategoryAncestorSerializer,
    CategorySerializer,
    ItemsSerializer,
    BenefitsSerializer,
)
from rest_framework import viewsets
from .models import Category, Items, Benefits
from django_filters import rest_framework as filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework import generics


# Create your views here.


class ItemFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="original_price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="original_price", lookup_expr="lte")

    class Meta:
        model = Items
        fields = [
            "min_price",
            "max_price",
            "category__name",
            "benefits__name",
        ]


class ItemsViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the items

    """

    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    filterset_class = ItemFilter

    search_fields = ("name",)
    # filterset_fields = ('name', 'price')

    # filterset_fields=('name')


class CategoryListView(generics.ListAPIView, generics.RetrieveAPIView):
    model = Category
    queryset = Category.objects.filter(level=0)
    serializer_class = CategorySerializer
    search_fields = ["name", "children__name"]


class BenefitsListView(APIView):
    def get(self, request):
        queryset = Benefits.objects.all()
        serializer = BenefitsSerializer(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data)


class categoryAncestorsView(APIView):
    def get(self, request, id):
        category_instance = Category.objects.get(id=id)
        ancestors = category_instance.get_ancestors(include_self=True)
        serializer = CategoryAncestorSerializer(
            ancestors, many=True, context={"request": request}
        )

        return Response(serializer.data)
