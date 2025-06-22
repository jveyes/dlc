import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from DLC.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("DLC/", include("DLC.urls")),
]

if settings.DEBUG: 
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]