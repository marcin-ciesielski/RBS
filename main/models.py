from django.db import models
from datetime import datetime

class Room(models.Model):
    name = models.CharField(max_length=64)
    capacity = models.IntegerField(null=True)
    projector = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    date = models.DateField(default=datetime.now)
    comment = models.CharField(max_length=256)
    rooms = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment