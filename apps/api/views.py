from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.response import Response


class ApiEndpointsOverview(ListAPIView):
    # DISPLAYS ALL API ENDPOINTS
    def get(self, request, *args, **kwargs):
        resp = dict()
        resp["message"] = "Success"
        resp["status_code"] = 200
        resp["Meta"] = "These are all the endpoints available on the mbari API"

        resp["endpoints"] = dict()
        resp["endpoints"]["magazine"] = dict()
        resp["endpoints"]["magazine"]["get_all_issues"] = "http://127.0.0.1:8000/v1/magazine/issues/"
        resp["endpoints"]["magazine"]["create_issue"] = "http://127.0.0.1:8000/v1/magazine/issues/"
        resp["endpoints"]["magazine"]["get_specific_issue_detail"] = "http://127.0.0.1:8000/v1/magazine/issues/:id/"
        resp["endpoints"]["magazine"]["get_specific_issue's_contributors"] = "http://127.0.0.1:8000/v1/magazine/issues/:id/contributors/"
        resp["endpoints"]["magazine"]["delete_issue"] = "http://127.0.0.1:8000/v1/magazine/issues/:id/delete/"
        resp["endpoints"]["magazine"]["update_issue"] = "http://127.0.0.1:8000/v1/magazine/issues/:id/update/"

        resp["endpoints"]["profiles"] = dict()
        resp["endpoints"]["profiles"]["get_all_users"] = "http://127.0.0.1:8000/v1/profiles/"
        resp["endpoints"]["profiles"]["create_a_user"] = "http://127.0.0.1:8000/v1/profiles/"
        resp["endpoints"]["profiles"]["get_a_specific_user_detail"] = "http://127.0.0.1:8000/v1/profiles/:id/"
        resp["endpoints"]["profiles"]["get_a_specific_user's_likes"] = "http://127.0.0.1:8000/v1/profiles/:id/likes/"
        resp["endpoints"]["profiles"]["get_a_specific_user's_posts"] = "http://127.0.0.1:8000/v1/profiles/:id/posts/"
        resp["endpoints"]["profiles"]["delete_a_specific_user"] = "http://127.0.0.1:8000/v1/profiles/:id/delete/"
        resp["endpoints"]["profiles"]["update_a_specific_user"] = "http://127.0.0.1:8000/v1/profiles/:id/update/"

        resp["endpoints"]["blog"] = dict()
        resp["endpoints"]["blog"]["get_all_posts"] = "http://127.0.0.1:8000/v1/blog/"
        resp["endpoints"]["blog"]["create_a_post_detail"] = "http://127.0.0.1:8000/v1/blog/"
        resp["endpoints"]["blog"]["get_a_specific_post"] = "http://127.0.0.1:8000/v1/blog/:id/"
        resp["endpoints"]["blog"]["delete_a_specific_post"] = "http://127.0.0.1:8000/v1/blog/:id/delete/"
        resp["endpoints"]["blog"]["update_a_specific_post"] = "http://127.0.0.1:8000/v1/blog/:id/update/"
        
        return Response(resp, status=status.HTTP_200_OK)
