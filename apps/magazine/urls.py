from django.urls import path, include
from .views import ApiEndpointsOverview


urlpatterns = [
    path("", ApiEndpointsOverview.as_view(), name="endpoints_overview"),
]
