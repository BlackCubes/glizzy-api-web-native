from django.urls import path

from . import views


urlpatterns = [
    path("", views.ReactionCreateView.as_view(), name="create"),
]
