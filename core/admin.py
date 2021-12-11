from django.contrib import admin
from core.models import Location, Item, DeviceType, Device, Device_Item

# Register your models here.


class LocationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "created_at", "updated_at")
    search_fields = ("id", "name", "description", "created_at", "updated_at")
    list_per_page = 25


class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "created_at", "updated_at")
    search_fields = ("id", "name", "description", "created_at", "updated_at")
    list_per_page = 25


class DeviceTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "created_at", "updated_at")
    search_fields = ("id", "name", "description", "created_at", "updated_at")
    list_per_page = 25


class DeviceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "created_at", "updated_at")
    search_fields = ("id", "name", "description", "created_at", "updated_at")
    list_per_page = 25


class Device_ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "device", "item", "created_at", "updated_at")
    search_fields = ("id", "device", "item", "created_at", "updated_at")
    list_per_page = 25


admin.site.register(Location, LocationAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(DeviceType, DeviceTypeAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Device_Item, Device_ItemAdmin)
