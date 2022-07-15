from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .forms import ReactionForm
from .models import Reaction


class ReactionAdmin(admin.ModelAdmin):
    """
    Main admin for the Reaction model.
    """

    model = Reaction
    form = ReactionForm

    # Viewing all reactions
    list_display = (
        "reaction_count",
        "link_to_emoji",
        "link_to_glizzy",
        "created_at",
        "updated_at",
    )
    list_display_links = ("reaction_count",)
    list_filter = (
        "reaction_count",
        "emoji",
        "glizzy",
    )
    search_fields = (
        "reaction_count",
        "emoji__emoji",
        "emoji__name",
        "product__name",
    )
    ordering = ("-reaction_count",)

    # Viewing and changing one reaction
    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "reaction_count",
                    "basic_info_detail",
                    "basic_info_note",
                )
            },
        ),
        (
            "Additional Info",
            {
                "fields": (
                    "id",
                    "uuid",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )
    readonly_fields = (
        "id",
        "uuid",
        "created_at",
        "updated_at",
        "basic_info_detail",
        "basic_info_note",
    )

    # Adding one new reaction
    add_fieldset = (
        (
            None,
            {
                "fields": {
                    "reaction_count",
                    "emoji",
                    "glizzy",
                }
            },
        ),
    )

    # Some additional info
    @admin.display(description="Detail")
    def basic_info_detail(self, obj):
        count_info_grammar = "are" if obj.reaction_count > 1 else "is"

        count_info_plural = "s" if obj.reaction_count > 1 else ""

        return format_html(
            f"<i>There {count_info_grammar} {obj.reaction_count} count{count_info_plural} of {obj.emoji.emoji}'s for the {obj.glizzy.name}.</i>"
        )

    @admin.display(description="Note")
    def basic_info_note(self, obj):
        return format_html(
            '<small style="font-weight: bold;">Cannot change the emoji or glizzy.</small>'
        )

    # To display the ``add_fieldset`` on the creation page
    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldset

        return super(ReactionAdmin, self).get_fieldsets(request, obj)

    # Custom link to the emoji's change page instead of the reaction change
    # page.
    @admin.display(description="Emoji")
    def link_to_emoji(self, obj):
        link = reverse("admin:emoji_emoji_change", args=[obj.emoji.id])

        return format_html('<a href="{}">{}</a>', link, obj.emoji)

    # Custom link to the glizzy's change page instead of the reaction change
    # page.
    @admin.display(description="Glizzy")
    def link_to_glizzy(self, obj):
        link = reverse("admin:glizzy_glizzy_change", args=[obj.glizzy.id])

        return format_html('<a href="{}">{}</a>', link, obj.glizzy)


admin.site.register(Reaction, ReactionAdmin)
