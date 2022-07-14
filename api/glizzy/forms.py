from django import forms

from .models import Glizzy
from .utils import model_error_messages


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
            "name": model_error_messages["name"],
            "short_info": model_error_messages["short_info"],
            "long_info": model_error_messages["long_info"],
            "image": model_error_messages["image"],
        }
