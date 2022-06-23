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
import django_filters
from django_filters.constants import EMPTY_VALUES


class ListFilter(filters.Filter):
    """
    Filter through comma seperated values
    eg:- &category=1,2,4
    """

    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs
        value_list = value.split(",")
        qs = super().filter(qs, value_list)
        return qs


class ItemFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="original_price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="original_price", lookup_expr="lte")
    category = ListFilter(field_name="category__name__in", lookup_expr="in")
    benefits = ListFilter(field_name="benefits__name__in", lookup_expr="in")

    class Meta:
        model = Items
        fields = [
            "min_price",
            "max_price",
            "category",
            "benefits",
        ]


class ItemsViewSet(viewsets.ModelViewSet):
    """
    #RestApi Endpoint for viewing and editing the items
    ## Api Actions Supported
    `GET`
    `POST`
    `PATCH`
    `UPDATE`
    `DELETE`

    """

    queryset = Items.objects.filter(active=True).all()
    serializer_class = ItemsSerializer
    filterset_class = ItemFilter

    search_fields = ("name",)
    # filterset_fields = ('name', 'price')

    # filterset_fields=('name')


class CategoryListView(
    generics.ListAPIView,
    generics.RetrieveAPIView,
    generics.CreateAPIView,
    generics.DestroyAPIView,
    generics.UpdateAPIView,
):
    """
    #RestApi Endpoint for viewing and editing the Category
    ## Api Actions Supported
    `GET`
    `POST`
    `UPDATE`
    `DELETE`

    """

    model = Category
    queryset = Category.objects.filter(level=0)
    serializer_class = CategorySerializer
    search_fields = ["name", "children__name"]


class BenefitsListView(APIView):
    """
    #RestApi Endpoint for getting Benefits
    ## Api Actions Supported
    `GET`
    """

    def get(self, request):
        queryset = Benefits.objects.all().order_by("name")
        serializer = BenefitsSerializer(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data)


class categoryAncestorsView(APIView):
    """
    #RestApi Endpoint for getting Category Ancestors
    ## Api Actions Supported
    `GET`
    """

    def get(self, request, id):
        category_instance = Category.objects.get(id=id)
        ancestors = category_instance.get_ancestors(include_self=True)
        serializer = CategoryAncestorSerializer(
            ancestors, many=True, context={"request": request}
        )

        return Response(serializer.data)
