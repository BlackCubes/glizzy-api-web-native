from django.urls import path

from . import views


app_name = "glizzy"

urlpatterns = [
    path("", views.GlizzyListView.as_view(), name="list"),
    path("<pk:pk>", views.GlizzyDetailView.as_view(), name="detail"),
    path("<slug:slug>", views.GlizzyDetailView.as_view(), name="detail"),
]
