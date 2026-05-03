from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('in_progress', 'In Progress'),
    ('delivered', 'Delivered'),
    ('cancelled', 'Cancelled'),
)

class TruckOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    pickup_location = models.CharField(max_length=255)
    delivery_location = models.CharField(max_length=255)
    shipment_size = models.CharField(max_length=100)
    shipment_weight = models.DecimalField(max_digits=10, decimal_places=2, help_text="Weight in kg")
    shipment_type = models.CharField(max_length=100)
    pickup_time = models.DateTimeField()
    delivery_time = models.DateTimeField(null=True, blank=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    admin_comment = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username} - {self.get_status_display()}"
