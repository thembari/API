from django.urls import path
from .views import *


urlpatterns = [
    path("issues/", IssuesListCreateView.as_view(), name="get_all_issues"),
    path("issues/", IssuesListCreateView.as_view(), name="create_new_issue"),
    path("issues/<uuid:id>/", IssueDetailUpdateView.as_view(), name="get_specific_issue"),
    path("issues/<uuid:id>/", IssueDetailUpdateView.as_view(), name="update_specific_issue"),
    path("issues/delete/<uuid:id>/", IssueDestroyView.as_view(), name="delete_specific_issue"),
]
