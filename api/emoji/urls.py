from django.urls import path

from . import views


app_name = "emoji"

urlpatterns = [
    path("", views.EmojiListView.as_view(), name="list"),
]
