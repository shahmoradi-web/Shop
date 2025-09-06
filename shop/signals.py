from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.timezone import is_naive

from .models import Product

@receiver(pre_save, sender=Product)
def calculate_price(sender, instance, **kwargs):
    instance.new_price = instance.price - instance.off