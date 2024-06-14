from django.contrib import admin

from reserve.models import Reserve


@admin.register(Reserve)
class ReserveAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'room',
                    'get_reservation_time_start', 'get_reservation_time_end')
    ordering = ['-id',]

    fieldsets = (
        ('Information', {'fields': ('room', 'name',)}),
        ("Time", {'fields': ('reservation_time_start', 'reservation_time_end')}),
    )

    add_fieldsets = (
        ('Information', {'fields': ('room', 'name',)}),
        ("Time", {'fields': ('reservation_time_start', 'reservation_time_end')}),
    )
