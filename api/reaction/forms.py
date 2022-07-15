from django import forms

from .models import Reaction
from .utils import model_error_messages


class ReactionForm(forms.ModelForm):
    """
    A ModelForm that maps all of the Reaction model fields with the given form
    fields of ``reaction_count``, ``emoji``, and ``glizzy``.

    Custom input labels are displayed for the ``reaction_count``, ``emoji``,
    and ``glizzy``.

    Lastly, custom error messages are displayed for the ``reaction_count``,
    ``emoji``, and ``glizzy``.
    """

    class Meta:
        model = Reaction

        fields = (
            "reaction_count",
            "emoji",
            "glizzy",
        )

        labels = {
            "reaction_count": "*Reaction count",
            "emoji": "*Emoji",
            "glizzy": "*Glizzy",
        }

        error_messages = {
            "reaction_count": model_error_messages["reaction_count"],
            "emoji": model_error_messages["emoji"],
            "glizzy": model_error_messages["glizzy"],
        }
