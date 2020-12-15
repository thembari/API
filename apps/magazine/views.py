from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.response import Response


class ApiEndpointsOverview(ListAPIView):
    def get(self, request, *args, **kwargs):
        resp = dict()
        resp["message"] = "Success"
        resp["status_code"] = 200
        resp["endpoints"] = dict()
        resp["endpoints"]["get_all_issues"] = "https://127.0.0.1/magazine/issues/"
        resp["endpoints"][
            "get_specific_issue"
        ] = "https://127.0.0.1/magazine/issues/<int:id>/"
        return Response(resp, status=status.HTTP_200_OK)
