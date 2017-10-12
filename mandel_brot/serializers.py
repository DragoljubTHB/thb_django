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
        print(kwargs)
        # drawing area
        xa = -2.0
        xb = 1.0
        ya = -1.5
        yb = 1.5
        maxIt = 100 #255  # max iterations allowed
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
        # self.content.seek(0)
        # self.image.save('/home/dado/thb/myImage2.png', "PNG")

    def in_bytes(self):
        # self.content.seek(0)
        return self.content.getbuffer()
# base64.b64encode(content.read()
# JSONRenderer()
# self.content.


class MandelbrotCustomSerializer(serializers.Serializer):

    # def update(self, instance, validated_data):
    #    pass
    # width = serializers.IntegerField()
    # height = serializers.IntegerField()
    # iterations = serializers.IntegerField()
    # print(width, height, iterations, sep=' ')

    def create(self, validated_data):
        print('create')
        print(self.context)
        # return Mandelbrot(width=validated_data['w'],height=validated_data['h'],iterations=validated_data['it']).image
        mandel = Mandelbrot(width=100, height=100, iterations=100).in_bytes()
        print(mandel)
        return mandel

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

