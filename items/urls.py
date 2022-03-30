from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryListView,
    ItemsViewSet,
    categoryAncestorsView,
    BenefitsListView,
)

router = DefaultRouter()
router.register("items", ItemsViewSet)
urlpatterns = [
    path("category/", CategoryListView.as_view()),
    path("benefits/", BenefitsListView.as_view()),
    path("category/ancestor/<int:id>", categoryAncestorsView.as_view()),
]
urlpatterns += router.urls
