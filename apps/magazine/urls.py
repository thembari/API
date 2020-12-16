from django.urls import path
from .views import IssuesListView


urlpatterns = [
    path("issues/", IssuesListView.as_view(), name="endpoints_overview"),
]
