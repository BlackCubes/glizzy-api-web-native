from django.shortcuts import get_object_or_404


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
            if self.kwargs[field]:
                field_filter[field] = self.kwargs[field]

        obj = get_object_or_404(queryset, **field_filter)

        self.check_object_permissions(self.request, obj)

        return obj
