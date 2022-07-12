from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Glizzy

from core.utils import slug_generator


@receiver(signal=pre_save, sender=Glizzy)
def create_slug(sender, instance):
    "Converts the string into a slug if it is not present."
    if not instance.slug:
        instance.slug = slug_generator(instance)
