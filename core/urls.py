import os

import decouple
from django.conf import settings
from django.contrib import admin
from django.urls import include, path


def get_admin_panel_url() -> str:
    """assign ADMIN_PANEL_URL envvar to admin_panel variable."""
    try:
        admin_panel_url = decouple.config("ADMIN_PANEL_URL")
    except decouple.UndefinedValueError:
        try:
            admin_panel_url = os.environ["ADMIN_PANEL_URLs"]
        except KeyError:
            raise Exception("ADMIN_PANEL_URL was not set as environment variable.")
    return admin_panel_url


urlpatterns = [
    path(get_admin_panel_url(), admin.site.urls),
    path("", include("portfolio.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
