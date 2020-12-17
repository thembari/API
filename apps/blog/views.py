from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from datetime import datetime
from .models import *

class ListUsersView(generics.ListAPIView):
    pass

class RetrieveUpdateDestroyUsersView(generics.RetrieveUpdateDestroyAPIView):
    pass
