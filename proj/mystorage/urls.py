from rest_framework.routers import DefaultRouter
from django.urls import path,include
from mystorage import views

router = DefaultRouter() #객체 생성
router.register('essay', views.PostViewSet) #views.py 에 Postviewset 클래스 에서 가져오기,
router.register('album', views.ImageViewSet) #views.py 에 Postviewset 클래스 에서 가져오기,
router.register('files', views.FileViewSet) #views.py 에 Postviewset 클래스 에서 가져오기,



urlpatterns = [
    path('', include(router.urls)),
]