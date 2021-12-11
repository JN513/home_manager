from django.urls import path, include
from core.views import (
    index,
    login,
    register,
    dashboard,
    create_location,
    locations,
    location,
    put_location,
    delete_location,
    create_item,
    itens,
    item,
    put_item,
    delete_item,
    create_device_type,
    device_types,
    device_type,
    put_device_type,
    delete_device_type,
    create_device,
    devices,
    device,
    put_device,
    delete_device,
)

urlpatterns = [
    path("", index, name="index"),
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("dashboard/", dashboard, name="dashboard"),
    path("locations/", locations, name="locations"),
    path("location/<int:id>/", location, name="location"),
    path("location/put/", put_location, name="put_location"),
    path("location/delete/<int:id>/", delete_location, name="delete_location"),
    path("create_location/", create_location, name="create_location"),
    path("itens/", itens, name="itens"),
    path("item/<int:id>/", item, name="item"),
    path("item/put/", put_item, name="put_item"),
    path("item/delete/<int:id>/", delete_item, name="delete_item"),
    path("create_item/", create_item, name="create_item"),
    path("device_types/", device_types, name="device_types"),
    path("device_type/<int:id>/", device_type, name="device_type"),
    path("device_type/put/", put_device_type, name="put_device_type"),
    path("device_type/delete/<int:id>/", delete_device_type, name="delete_device_type"),
    path("create_device_type/", create_device_type, name="create_device_type"),
    path("devices/", devices, name="devices"),
    path("device/<int:id>/", device, name="device"),
    path("device/put/", put_device, name="put_device"),
    path("device/delete/<int:id>/", delete_device, name="delete_device"),
    path("create_device/", create_device, name="create_device"),
]