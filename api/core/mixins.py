from rest_framework.exceptions import NotFound


class MultipleFieldLookupMixin:
    """
    Custom mixin to any view or viewset to get multiple field filtering on a
    ``lookup_fields`` attribute, instead of the default single field
    filtering.

    NOTE: Taken from the Django REST Framework docs:
    https://www.django-rest-framework.org/api-guide/generic-views/#creating-custom-mixins
    """

    def get_object(self):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)

        field_filter = {}

        for field in self.lookup_fields:
            if self.kwargs.get(field, None):
                field_filter[field] = self.kwargs[field]

        try:
            obj = queryset.get(**field_filter)
        except queryset.model.DoesNotExist:
            model_name = queryset.model.__name__

            raise NotFound(f"The {model_name.lower()} does not exist.")

        self.check_object_permissions(self.request, obj)

        return obj
