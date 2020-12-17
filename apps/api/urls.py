from django.urls import path
from .views import ApiEndpointsOverview

urlpatterns = [
    path("", ApiEndpointsOverview.as_view(), name="endpoints_overview"),
]
