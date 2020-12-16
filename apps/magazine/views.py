from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.response import Response


class IssuesListView(RetrieveAPIView):
    # DISPLAYS ALL MAGAZINE ISSUES
    def get(self, request, *args, **kwargs):
        resp = dict()
        resp["message"] = "Success"
        resp["status_code"] = 200
        resp["issues"] = dict()

        return Response(resp, status=status.HTTP_200_OK)
