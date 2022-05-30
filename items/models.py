from tabnanny import verbose
from unicodedata import name
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    name_discription = models.TextField(null=True, blank=True)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    parent_discription = models.TextField(null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self) -> str:
        return self.name


class Items(models.Model):
    name = models.CharField(max_length=50, unique=True)
    owner = models.ForeignKey("Owners", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    original_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    original_price_from = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    original_price_to = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    price_range_from = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    price_range_to = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    reviews_score = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )

    count_of_reviews = models.IntegerField(null=True, blank=True)
    img_source_link = models.URLField(null=True, blank=True)
    link_to_item = models.URLField(null=True, blank=True)
    category = models.ManyToManyField(Category, null=True, blank=True)
    benefits = models.ManyToManyField(
        "Benefits",
    )
    description = models.TextField(null=True, blank=True)
    popular_ind = models.IntegerField(
        null=True,
        blank=True,
        max_length=100,
    )
    recent_customer_name = models.CharField(max_length=50, null=True, blank=True)
    recent_customer_title = models.CharField(max_length=255, null=True, blank=True)
    recent_customer_desc = models.TextField(null=True, blank=True)
    recent_customer_score = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    active = models.BooleanField(default=False)

    def Categories(self):
        return "\n \t || ".join([p.name for p in self.category.all()])

    def BeneFits(self):
        return "\n\t || ".join([p.name for p in self.benefits.all()])

    class Meta:
        verbose_name_plural = "Items"
        verbose_name = "Item"

    def __str__(self) -> str:
        return self.name


class Owners(models.Model):
    name = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    owner_affilaite_program_id = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = "Owner"
        verbose_name_plural = "Owners"

    def __str__(self) -> str:
        return self.name


class Benefits(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Benefits"
        verbose_name = "Benefit"

    def __str__(self) -> str:
        return self.name
