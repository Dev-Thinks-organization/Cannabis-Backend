from django.contrib import admin
from .models import Category, Items, Owners, Benefits
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from django.urls import path
from django.shortcuts import render
from django import forms
import pandas as pd
import pprint

# register all the models in the admin page
admin.site.register(Category, DraggableMPTTAdmin)

admin.site.register(Owners)
admin.site.register(Benefits)


class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


class ItemsAdmin(admin.ModelAdmin):
    list_display = ("name", "id")

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path("upload-csv/", self.upload_csv),
        ]
        return new_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            file_data = pd.read_excel(csv_file, sheet_name="ownerid=1")
            excel_data = list()
            # print(file_data)
            # print(file_data)
            df = pd.DataFrame(
                file_data,
                # columns=[
                #     "Aff link to product ",
                #     "Image source link",
                #     "count of reviews ",
                # ],
            )
            # print(df.columns)
            # print(df.values)

            for i in df.values:
                print(i[11], "-----------")
                created = Items.objects.update_or_create(
                    link_to_item=i[0],
                    img_source_link=i[1],
                    count_of_reviews=i[3],
                    reviews_score=i[4],
                    description=i[5],
                    benefits=i[6],
                    category=i[7],
                    price_range_to=i[8],
                    price_range_from=i[9],
                    original_price_to=i[10],
                    original_price_from=i[11],
                    price=i[12],
                    original_price=i[13],
                    title=i[14],
                    id=i[15]
                    # category = CBD i[12]
                )
            url = reverse("admin:index")
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)


admin.site.register(Items, ItemsAdmin)
