from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *
from pprint import pprint


# VIEW CLASS FOR LISTING AND CREATING NEW POSTS
class IssuesListCreateView(generics.ListCreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueModelSerializer

    # DISPLAYS ALL MAGAZINE ISSUES
    def get(self, request, *args, **kwargs):

        serializer = IssueModelSerializer
        issues = Issue.objects.all()
        serializer = serializer(issues, many=True)
        resp = dict()
        resp["message"] = "Success"
        resp["status_code"] = 200
        resp["issues"] = dict()
        for issue in serializer.data:
            resp["issues"][issue.get('title').title()] = issue
            # resp["issues"][issue.get('title').title()]['content'] = issue_content
        return Response(resp, status=status.HTTP_200_OK)


    # CREATE NEW MAGAZINE ISSUE
    def post(self, request, *args, **kwargs):

        serializer = IssueModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            resp = dict()
            resp["message"] = "Success"
            resp["status_code"] = 201

            return Response(resp, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


# VIEW CLASS FOR DETAIL VIEW AND UPDATE OF ISSUE
class IssueDetailUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueModelSerializer

    def get(self, request, *args, **kwargs):
        issue = Issue.objects.get(id=self.kwargs['id'])
        contents = Content.objects.filter(issue=self.kwargs['id'])
        serializer = ContentModelSerializer(contents, many=True)

        serializer1 = IssueModelSerializer
        serializer1 = serializer1(issue)
        resp = dict()
        resp["message"] = "Success"
        resp["status_code"] = 200
        resp[str(issue).title()] = serializer1.data
        resp['contents'] = list()

        for item in contents.iterator():
            all_contributors = item.contributors.all()
            all_categories = item.category.all()
            # print(type(item.image))
            content_obj = dict(
                title = item.title,
                content = item.content,
                image = item.image.url,
                contributors = [str(contributor) for contributor in all_contributors],
                categories = [str(category) for category in all_categories],

            )

            resp['contents'].append(content_obj)
        return Response(resp, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):

        serializer = IssueModelSerializer
        issue = Issue.objects.get(id=self.kwargs['id'])
        serializer = serializer(issue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            resp = dict()
            resp["message"] = 'Updated'
            resp["status_code"] = status.HTTP_200_OK
            return Response(resp, status=status.HTTP_200_OK)


# VIEW CLASS FOR DELETING AN ISSUE
class IssueDestroyView(generics.DestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueModelSerializer

    def delete(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, id=self.kwargs['id'])


        issue.delete()
        resp = dict()
        resp["message"] = 'Deleted'
        resp["status_code"] = status.HTTP_204_NO_CONTENT
        return Response(resp, status=status.HTTP_204_NO_CONTENT)
