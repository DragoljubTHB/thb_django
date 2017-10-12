"""dj_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from mandel_brot.views import ImageView, UserViewSet
router = DefaultRouter()

# router.register(r'^mandelbrot', viewset=ImageView.as_view(), base_name='mandelbrot')
router.register(r'^users', viewset=UserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Mandelbrot/getMandelbrot?w=800&h=600&it=1000
     url(r'^Mandelbrot/getMandelbrot', view=ImageView.as_view()),
    # url(r'^Mandelbrot/getMandelbrot', view=ImageView2.as_view()),
    # REST-----
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
]
