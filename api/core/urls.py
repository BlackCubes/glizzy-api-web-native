"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from strawberry.django.views import GraphQLView

from .graphql_config import schema

urlpatterns = [
    path("admin/", admin.site.urls),
    # Rest APIs
    path("api/v1/emojis/", include("emoji.urls")),
    path("api/v1/glizzys/", include("glizzy.urls")),
    path("api/v1/reactions/", include("reaction.urls")),
    # GraphQL
    path(
        "graphql/", GraphQLView.as_view(schema=schema, graphiql=settings.DEBUG)
    ),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )


handler404 = "core.utils.error_404"
handler500 = "core.utils.error_500"
