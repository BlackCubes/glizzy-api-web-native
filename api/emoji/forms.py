from django import forms

from .models import Emoji
from .utils import model_error_messages


class EmojiForm(forms.ModelForm):
    """
    A ModelForm that maps all of the Emoji model fields with the given form
    fields of ``name`` and ``emoji``.

    Custom input labels are displayed for the ``name`` and ``emoji``.

    Custom widgets are also displayed for the ``name`` and ``emoji``.

    Lastly, custom error messages are displayed for the ``name`` and
    ``emoji``.
    """

    emoji = forms.CharField(
        max_length=2,
        label="*Emoji",
        widget=forms.TextInput(attrs={"placeholder": "🌭"}),
        error_messages=model_error_messages["emoji"],
    )

    class Meta:
        model = Emoji

        fields = (
            "name",
            "emoji",
        )

        labels = {"name": "*Name"}

        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "A lit name for the emoji"}
            )
        }

        error_messages = {"name": model_error_messages["name"]}
