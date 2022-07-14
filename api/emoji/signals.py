from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Emoji

from core.utils import slug_generator


@receiver(signal=pre_save, sender=Emoji)
def create_slug(sender, instance, **kwargs):
    """
    Converts the string into a slug if it is not present.
    """

    if not instance.slug:
        instance.slug = slug_generator(instance)
