import random
import string
from django.utils.text import slugify


def random_string_generator(
    size=10, chars=string.ascii_lowercase + string.digits
):
    """
    Generates a random string.
    """
    return "".join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """
    Assumes the instance has a model with ``slug`` and ``name`` fields.

    Returns a unique slug from the model's ``name`` field if the ``slug``
    query exists in the DB, or the newly created ``slug`` that slugifies the
    model's name if the ``slug`` query does not exist in the DB.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)

    model = instance.__class__
    query_exists = model.objects.filter(slug=slug).exists()

    if query_exists:
        unique_slug = "{slug}-{randstr}".format(
            slug=slug, randstr=random_string_generator(size=4)
        )

        # Run this function again to check if the uniquely random slug is
        # truly unique in the DB. If it is unique, return the unique slug.
        # Otherwise, generate another unique slug.
        return unique_slug_generator(instance, new_slug=unique_slug)

    return slug
