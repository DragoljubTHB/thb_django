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
        print('views get')
        # mandel = Mandelbrot()
        # return Response(mandel, status=status.HTTP_201_CREATED, content_type="image/png")
        print(request.query_params)
        # mandelbrot_custom_serializer = MandelbrotCustomSerializer(data=request.query_params)
        # if mandelbrot_custom_serializer.is_valid():
        # mandelbrot_custom_serializer.is_valid()
        # mandel_image = mandelbrot_custom_serializer.save()
        # print(type(mandel_image))

        # return Response(mandel_image, status=status.HTTP_201_CREATED, content_type="image/png")
        # return Response(request.query_params, status=status.HTTP_400_BAD_REQUEST)
        return HttpResponse(Mandelbrot(width=request.query_params['w'],
                                   height=request.query_params['h'],
                                   iterations=100).in_bytes()
                        , status=status.HTTP_201_CREATED, content_type="image/png")



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

