from django.db import models

# Create your models here.

class Station(models.Model):
    empty_slots = models.IntegerField()
    free_bikes = models.IntegerField()
    id = models.UUIDField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.name


class Extra(models.Model):
    station = models.OneToOneField(Station, on_delete=models.CASCADE)

    address = models.CharField(max_length=100)
    altitude = models.FloatField()
    ebikes = models.IntegerField()
    has_ebikes = models.BooleanField()
    last_updated = models.IntegerField()
    normal_bikes = models.IntegerField()
    payment_terminal = models.BooleanField()
    post_code = models.IntegerField(null=True, default=0)
    renting = models.IntegerField()
    returning = models.IntegerField()
    slots = models.IntegerField()
    uid = models.IntegerField()

    def __str__(self) -> str:
        return self.station.name + ', ' + self.address

class Payment(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.station.name + ', ' + self.payment_method
