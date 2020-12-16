from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("/v1/api/", include("apps.api.urls")),
    path("/v1/magazine/", include("apps.magazine.urls")),
    path("/v1/store/", include("apps.store.urls")),
    path("/v1/profiles/", include("apps.profiles.urls")),
    path("/v1/blog/", include("apps.blog.urls")),
]
