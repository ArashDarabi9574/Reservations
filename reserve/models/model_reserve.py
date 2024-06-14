from django.db import models


class Reserve(models.Model):
    class Meta:
        verbose_name = 'Reserve'
        verbose_name_plural = 'Reserves'
        ordering = ['-id']

    room = models.ForeignKey(
        "Room", on_delete=models.CASCADE, related_name="room_reserves", verbose_name="Room Number")
    name = models.CharField(('name'), max_length=64, null=True, blank=True)
    reservation_time_start = models.DateTimeField(
        ('reservation_time_start'), null=True)
    reservation_time_end = models.DateTimeField(
        ('reservation_time_end'), null=True)

    def __str__(self):
        return self.name

    @property
    def get_reservation_time_start(self):
        if self.reservation_time_start:
            return self.reservation_time_start.strftime('%H:%M - %Y/%m/%d')

    @property
    def get_reservation_time_end(self):
        if self.reservation_time_end:
            return self.reservation_time_end.strftime('%H:%M - %Y/%m/%d')
