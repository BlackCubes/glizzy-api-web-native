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


# To keep things DRY
model_error_messages = {
    "uuid": {"unique": "The uuid is not unique."},
    "name": {
        "blank": "The name cannot be empty.",
        "max_length": "The name should be no more than 100 characters.",
        "required": "The name is required.",
        "unique": "The name already exists.",
    },
    "slug": {
        "max_length": "The slug should be no more than 100 characters.",
    },
    "short_info": {
        "blank": "The short info cannot be empty.",
        "max_length": "The short info should be no more than 200 characters.",
        "required": "The short info is required.",
    },
    "long_info": {
        "blank": "The long info cannot be empty.",
        "required": "The long info is required.",
    },
    "image": {
        "blank": "The image cannot be empty.",
        "required": "The image is required.",
    },
}
