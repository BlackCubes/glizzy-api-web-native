from django.urls import path, re_path

from . import views


app_name = "glizzy"

# NOTE: For the detail views, the user has the option to append a trailing
# slash or not. This is bad for SEO, but since these views are APIs and not
# server-side rendering, then it wouldn't matter to have a trailing slash for
# better user/developer experience.
urlpatterns = [
    path("", views.GlizzyListView.as_view(), name="list"),
    re_path(
        r"^(?P<pk>[0-9]+)/?$", views.GlizzyDetailView.as_view(), name="detail"
    ),
    re_path(
        r"^(?P<slug>[\w-]+)/?$",
        views.GlizzyDetailView.as_view(),
        name="detail",
    ),
]
