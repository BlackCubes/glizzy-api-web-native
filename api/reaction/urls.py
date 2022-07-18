from django.urls import path

from . import views


urlpatterns = [
    path("", views.ReactionListCreateView.as_view(), name="list-create"),
]
