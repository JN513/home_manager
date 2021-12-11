from django.shortcuts import render, redirect, get_object_or_404
from core.models import Location, Item, DeviceType, Device, Device_Item
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, "pages/index.html")


def login(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')

    return render(request, "pages/login.html")


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    return render(request, "pages/register.html")


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "pages/dashboard.html")


def create_location(request):
    if not request.user.is_authenticated:
        return redirect('login')
        
    return render(request, "pages/create_location.html")


def locations(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "pages/locations.html")


def location(request, id):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "pages/location.html")


def put_location(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "pages/put_location.html")


def delete_location(request, id):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "pages/delete_location.html")


def create_item(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "pages/create_item.html")


def itens(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "pages/itens.html")


def item(request, id):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "pages/device.html")


def put_item(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "pages/put_item.html")


def delete_item(request, id):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "pages/delete_item.html")


def create_device_type(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "pages/create_device_type.html")


def device_types(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "pages/device_types.html")


def device_type(request, id):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "pages/device_type.html")


def put_device_type(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "pages/put_device_type.html")


def delete_device_type(request, id):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "pages/delete_device_type.html")


def create_device(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "pages/create_device.html")


def devices(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "pages/devices.html")


def device(request, id):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "pages/device.html")


def put_device(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "pages/put_device.html")


def delete_device(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
        
    return render(request, "pages/delete_device.html")
