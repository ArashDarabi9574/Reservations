from django.db import models


class Room(models.Model):
    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'
        ordering = ['-id']

    room_number = models.PositiveIntegerField(('label'),
                                              blank=True, null=True)
    label = models.CharField(('label'), max_length=64)

    def __str__(self) -> str:
        return str(self.room_number)
