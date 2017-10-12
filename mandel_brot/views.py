from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework import views, viewsets, status
from rest_framework.response import Response

from mandel_brot.serializers import UserSerializer, MandelbrotCustomSerializer, Mandelbrot


class ImageView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        return HttpResponse(Mandelbrot(width=request.query_params['w'],
                                       height=request.query_params['h'],
                                       iterations=request.query_params['it']).in_bytes()
                            , status=status.HTTP_201_CREATED, content_type="image/png")


class ImageView2(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        print(request.query_params)
        serializer = MandelbrotCustomSerializer(
            data=request)
        if serializer.is_valid():
            mandel_image = serializer.save()

            return HttpResponse(mandel_image, status=status.HTTP_201_CREATED, content_type="image/png")
        return Response(request.query_params, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
