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
        resp["endpoints"] = dict()
        resp["endpoints"]["get_all_issues"] = "https://127.0.0.1/v1/magazine/issues/"
        resp["endpoints"][
            "get_specific_issue"
        ] = "https://127.0.0.1/v1//magazine/issues/:id/"
        resp["endpoints"]["store"] = "https://127.0.0.1/v1/store"
        return Response(resp, status=status.HTTP_200_OK)
