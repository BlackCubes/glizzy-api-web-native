import os
from django.utils import timezone


def upload_glizzy_image_to(instance, filename):
    """
    Changes the output of the image name.
    """
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000

    return f"images/glizzy/{instance.name}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"
