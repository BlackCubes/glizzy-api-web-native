from django.contrib import admin
from django.utils.html import format_html

from .forms import GlizzyForm
from .models import Glizzy


class GlizzyAdmin(admin.ModelAdmin):
    """
    Main admin for the Glizzy model.
    """

    model = Glizzy
    form = GlizzyForm

    # Viewing all glizzys
    list_display = (
        "name",
        "image_thumbnail_tag",
        "created_at",
        "updated_at",
    )
    list_display_links = (
        "name",
        "image_thumbnail_tag",
    )
    list_filter = ("name",)
    search_fields = ("name",)
    ordering = ("name",)

    # Viewing and changing one glizzy
    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "short_info",
                    "long_info",
                )
            },
        ),
        ("Glizzy Image", {"fields": ("image", "image_large_tag")}),
        (
            "Additional Info",
            {
                "fields": (
                    "uuid",
                    "slug",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )
    readonly_fields = (
        "uuid",
        "slug",
        "created_at",
        "updated_at",
        "image_large_tag",
    )

    # Adding one new glizzy
    add_fieldset = (
        (
            None,
            {
                "fields": (
                    "name",
                    "short_info",
                    "long_info",
                )
            },
        ),
    )

    # To display the ``add_fieldset`` on the creation page
    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldset

        return super(GlizzyAdmin, self).get_fieldsets(request, obj)

    # Adding preview images
    @admin.display(description="Preview")
    def image_large_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{0}" style="width: 100px; height: 100px;" />'.format(
                    obj.image.url
                )
            )
        else:
            return format_html("<b>(No image)</b>")

    @admin.display(description="Image")
    def image_thumbnail_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{0}" style="width: 45px; height: 45px;" />'.format(
                    obj.image.url
                )
            )
        else:
            return format_html("<b>(No image)</b>")


admin.site.register(Glizzy, GlizzyAdmin)
