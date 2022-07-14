from django.contrib import admin

from .forms import EmojiForm
from .models import Emoji


class EmojiAdmin(admin.ModelAdmin):
    """
    Main admin for the Emoji model.
    """

    model = Emoji
    form = EmojiForm

    # Viewing all emojis
    list_display = (
        "emoji",
        "name",
        "created_at",
        "updated_at",
    )
    list_display_links = (
        "emoji",
        "name",
    )
    list_filter = (
        "emoji",
        "name",
    )
    search_fields = (
        "emoji",
        "name",
    )
    ordering = ("name",)

    # Viewing and changing one emoji
    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "emoji",
                    "name",
                )
            },
        ),
        (
            "Additional Info",
            {
                "fields": (
                    "id",
                    "uuid",
                    "slug",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )
    readonly_fields = (
        "id",
        "uuid",
        "slug",
        "created_at",
        "updated_at",
    )

    # Adding one new emoji
    add_fieldset = (
        (
            None,
            {
                "fieldset",
                (
                    "emoji",
                    "name",
                ),
            },
        ),
    )

    # To display the ``add_fieldset`` on the creation page
    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldset

        return super(EmojiAdmin, self).get_fieldsets(request, obj)


admin.site.register(Emoji, EmojiAdmin)
