from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import static, status

from .models import User
from .serializers import UserSerializer

import json


@api_view(['GET'])
def get_user(request):

    if request.method == 'GET':
        user = User.objects.all()

        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)
