from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response

# Create your views here.

class HelloAuthView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        return Response(data={'message': 'Hello, world!'}, status=status.HTTP_200_OK)
