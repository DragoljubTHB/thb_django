from django.contrib.auth.models import User
from rest_framework import serializers

import pylab
import PIL
from PIL import ImageDraw
from PIL import Image
from io import BytesIO, StringIO

class Mandelbrot(object):

    image = None
    content = None

    def __init__(self, **kwargs):
        self.width = kwargs.get('width')
        self.height = kwargs.get('height')
        self.iterations = kwargs.get('iterations')
        # drawing area
        xa = -2.0
        xb = 1.0
        ya = -1.5
        yb = 1.5
        maxIt = int(self.iterations) #255  # max iterations allowed
        # image size
        imgx = int(self.width) # 512
        imgy = int(self.height) # 512
        self.image = Image.new("RGB", (imgx, imgy))

        for y in range(imgy):
            zy = y * (yb - ya) / (imgy - 1) + ya
            for x in range(imgx):
                zx = x * (xb - xa) / (imgx - 1) + xa
                z = zx + zy * 1j
                c = z
                for i in range(maxIt):
                    if abs(z) > 2.0: break
                    z = z * z + c
                self.image.putpixel((x, y), (i % 4 * 64, i % 8 * 32, i % 16 * 16))

        self.content = BytesIO()
        self.image.save(self.content, 'PNG')

    def in_bytes(self):
        return self.content.getbuffer()


class MandelbrotCustomSerializer(serializers.Serializer):

    def create(self, validated_data):
        return Mandelbrot(width=600, height=100, iterations=100).in_bytes()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

