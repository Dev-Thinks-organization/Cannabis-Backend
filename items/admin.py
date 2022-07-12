from django.contrib import admin
from .models import Category, Items, Owners, Benefits
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from django.urls import path
from django.shortcuts import render
from django import forms
import pandas as pd
import pprint

# register all the models in the admin page


class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


@admin.action(description="Mark selected Items as Active")
def make_active(modeladmin, request, queryset):
    queryset.update(active=True)


@admin.action(description="Mark selected Items as InActive")
def make_in_active(modeladmin, request, queryset):
    queryset.update(active=False)


class ItemsAdmin(admin.ModelAdmin):
    list_display = ("name", "BeneFits", "Categories", "owner", "id", "active")
    search_fields = (
        "name",
        "owner__name",
        "price",
        "created_at",
    )
    list_filter = (
        "category",
        "benefits",
        "owner",
    )
    actions = [make_active, make_in_active]

    # def get_urls(self):
    #     urls = super().get_urls()
    #     new_urls = [
    #         path("upload-csv/", self.upload_csv),
    #     ]
    #     return new_urls + urls

    # def upload_csv(self, request):
    #     if request.method == "POST":
    #         csv_file = request.FILES["csv_upload"]
    #         file_data = pd.read_excel(csv_file, sheet_name="ownerid=1")
    #         excel_data = list()
    #         # print(file_data)
    #         # print(file_data)
    #         df = pd.DataFrame(
    #             file_data,
    #             # columns=[
    #             #     "Aff link to product ",
    #             #     "Image source link",
    #             #     "count of reviews ",
    #             # ],
    #         )
    #         # print(df.columns)
    #         # print(df.values)

    #         for i in df.values:
    #             print(i[11], "-----------")
    #             created = Items.objects.update_or_create(
    #                 link_to_item=i[0],
    #                 img_source_link=i[1],
    #                 count_of_reviews=i[3],
    #                 reviews_score=i[4],
    #                 description=i[5],
    #                 benefits=i[6],
    #                 category=i[7],
    #                 price_range_to=i[8],
    #                 price_range_from=i[9],
    #                 original_price_to=i[10],
    #                 original_price_from=i[11],
    #                 price=i[12],
    #                 original_price=i[13],
    #                 title=i[14],
    #                 id=i[15]
    #                 # category = CBD i[12]
    #             )
    #         url = reverse("admin:index")
    #         return HttpResponseRedirect(url)

    #     form = CsvImportForm()
    #     data = {"form": form}
    #     return render(request, "admin/csv_upload.html", data)


class OwnerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "url",
    )
    search_fields = (
        "name",
        "location",
        "url",
    )
    search_help_text = (
        ' You can Search By "owner_affilaite_program_id","location","url"'
    )


admin.site.register(Items, ItemsAdmin)
admin.site.register(Category, DraggableMPTTAdmin)

admin.site.register(Owners, OwnerAdmin)
admin.site.register(Benefits)
