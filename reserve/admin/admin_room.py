from django.contrib import admin

from reserve.models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'room_number', 'label')
    ordering = ['-id', ]

    fieldsets = (
        ('Information', {'fields': ('room_number', 'label')}),
    )

    add_fieldsets = (
        ('Information', {'fields': ('room_number', 'label')}),
    )
