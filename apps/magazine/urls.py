from django.urls import path
from .views import IssuesListView


urlpatterns = [
    path("issues/", IssuesListView.as_view(), name="get_all_issues"),
]
