from django.contrib import admin
from django.urls import path,include
from mystorage import urls # 스타트앱의 urls 연결.
from rest_framework import urls #rest프레임워크 url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mystorage.urls')),
    path('api_auth/',include('rest_framework.urls')), #rest프레임워크 로그인기능 구현

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) #미디어 파일이 담길곳