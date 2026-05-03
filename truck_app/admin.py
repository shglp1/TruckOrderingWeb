from django.contrib import admin
from .models import TruckOrder

@admin.register(TruckOrder)
class TruckOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'pickup_location', 'delivery_location', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'user')
    search_fields = ('user__username', 'pickup_location', 'delivery_location', 'id')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('User Information', {
            'fields': ('user',)
        }),
        ('Order Details', {
            'fields': ('pickup_location', 'delivery_location', 'shipment_size', 'shipment_weight', 'shipment_type')
        }),
        ('Timing', {
            'fields': ('pickup_time', 'delivery_time')
        }),
        ('Status & Admin', {
            'fields': ('status', 'admin_comment')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        })
    )
