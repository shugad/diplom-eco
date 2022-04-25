from django.contrib import admin
from .models import Region
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class RegionResource(resources.ModelResource):

    class Meta:
        model = Region


class RegionAdmin(ImportExportModelAdmin):
    resource_class = RegionResource


admin.site.register(Region, RegionAdmin)
