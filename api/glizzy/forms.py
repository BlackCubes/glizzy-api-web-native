from django import forms

from .models import Glizzy


class GlizzyForm(forms.ModelForm):
    """
    A ModelForm that maps all of the Glizzy model fields with the given form
    fields of ``name``, ``short_info``, ``long_info``, and ``image``.

    Custom input labels are displayed for the ``name``, ``short_info``,
    ``long_info``, and ``image``.

    Custom widgets are also displayed for the ``name``, ``short_info``, and
    ``long_info``.

    Lastly, custom error messages are displayed for the ``name``,
    ``short_info``, ``long_info``, and ``image``.
    """

    class Meta:
        model = Glizzy

        fields = (
            "name",
            "short_info",
            "long_info",
            "image",
        )

        labels = {
            "name": "*Name",
            "short_info": "*Short info",
            "long_info": "*Long info",
            "image": "*Image",
        }

        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "A beautiful glizzy name"}
            ),
            "short_info": forms.TextInput(
                attrs={"placeholder": "A short info for the glizzy"}
            ),
            "long_info": forms.Textarea(
                attrs={"placeholder": "A long and tasty info for the glizzy"}
            ),
        }

        error_messages = {
            "name": {
                "blank": "The name cannot be empty.",
                "max_length": "The name should be no more than 100 characters.",
                "required": "The name is required.",
                "unique": "The name already exists.",
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
