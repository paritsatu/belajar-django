
from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/',include('blog.urls',namespace='blog')),# dan yang spesifik kita kasi namespace
    url(r'^$',views.index,name='index')# berarti ini yang utama
]
