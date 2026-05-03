from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import TruckOrder

@receiver(pre_save, sender=TruckOrder)
def order_status_changed(sender, instance, **kwargs):
    if instance.id:
        try:
            old_instance = TruckOrder.objects.get(id=instance.id)
            if old_instance.status != instance.status or old_instance.admin_comment != instance.admin_comment:
                send_mail(
                    subject=f'Update on your Truck Order #{instance.id}',
                    message=f'Hello {instance.user.username},\n\nYour order status is now: {instance.get_status_display()}.\n\nAdmin Comment: {instance.admin_comment or "No comment."}\n\nThank you for using our service!',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[instance.user.email],
                    fail_silently=True,
                )
        except TruckOrder.DoesNotExist:
            pass
