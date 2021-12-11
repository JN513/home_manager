from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cordenadas = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    qtd = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images/")
    description = models.TextField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    state = models.BooleanField(default=True)
    price = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return super().__str__()


class DeviceType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=100)
    ip = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True, null=True)
    type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    mac_sta = models.CharField(max_length=100, blank=True)
    mac_ap = models.CharField(max_length=100, blank=True)
    location = models.ForeignKey(
        Location, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return super().__str__()


class Device_Item(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    qtd = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return super().__str__()
