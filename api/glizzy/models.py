from django.db import models
from uuid import uuid4

from .utils import model_error_messages, upload_glizzy_image_to


class Glizzy(models.Model):
    """
    Glizzy model with fields of ``uuid``, ``name``, ``slug``, ``short_info``,
    ``long_info``, ``image``, ``created_at``, and ``updated_at``.

    The ``uuid`` field is autogenerated during creation.

    The ``slug`` field is autogenerated during the pre_save signal.

    The ``created_at`` field is autogenerated during creation and only once.

    The ``updated_at`` field is autogenerated during creation and subsequently
    when the model is changed.
    """

    uuid = models.UUIDField(
        unique=True,
        default=uuid4,
        editable=False,
        error_messages=model_error_messages["uuid"],
    )
    name = models.CharField(
        max_length=100,
        unique=True,
        error_messages=model_error_messages["name"],
    )
    slug = models.SlugField(
        max_length=100,
        null=True,
        blank=True,
        error_messages=model_error_messages["slug"],
    )
    short_info = models.CharField(
        max_length=200,
        error_messages=model_error_messages["short_info"],
    )
    long_info = models.TextField(
        error_messages=model_error_messages["long_info"]
    )
    image = models.ImageField(
        upload_to=upload_glizzy_image_to,
        error_messages=model_error_messages["image"],
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Glizzy"
