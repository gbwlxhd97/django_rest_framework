from rest_framework import viewsets
from .models import Essay,Album,Files #models 에 의한 에세이 앨범 파일 임포트해주기.
from .serializers import EssaySerializer,AlbumSerializer,FilesSerializer
from rest_framework.filters import SearchFilter #검색어 기능 추가
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
class PostViewSet(viewsets.ModelViewSet):
    queryset = Essay.objects.all()
    serializer_class = EssaySerializer

    filter_backends = [SearchFilter] #search
    search_fields = ('title', 'body') #검색기능 추가 바디 타이틀에서 검색.

    def perform_create(self,serializer):
        serializer.save(author=self.request.user)#내가지금 작성한 그 유저로서 사용자를 저장해줌.

    

    def get_queryset(self): #로그인 기능중에서,필터링 해주는 함수.
        qs = super().get_queryset() #슈퍼클래스에 있는 쿼리셋을 받아온다음 변수에 넣기
        if self.request.user.is_authenticated:
            qs = qs.filter(author = self.request.user) # 위에 주석처럼 지금 author인 유저의 게시글만 필터링 해주기.
        else:
            qs = qs.none() #만약 로그아웃되어있는 유저라면 쿼리셋은 none으로 리턴. 
        return qs #쿼리셋 필터링 진행

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer

     #파일업로드 해결 방법.
    # parser_class 지정 5번쨰줄 에 임포트해줘야함
    parser_classes = (MultiPartParser, FormParser) 
    # create() 오버라이딩 시켜줘야함. 즉 크리에에이트는 post() 함수임
    # Api http -> get(), post()
    # *args 는 튜플로 출력 ** 둘다 가변인자임
    # **kwargs는 딕셔너리 형태로 출력

    # post 같은 http 메소드를 커스터마이징 시키려면 reponse와 status를 임포트 시켜야함 6,7번줄
    # 왜냐하면 내가 직접 http 메소드를 만들어주기 떄문임. 그렇기 떄문에 response가 필요해요
    def post(self, request,*args,**kwargs):
        serializer = FilesSerializer(data=request.data) #직접만들어주는 파일데이터
        if serializer.is_valid():
            serializer.save()  #유효성 검사를 통해 판별후 저장
            return Response(serializer.data, status=HTTP_201_CREATED) #유효한 데이터는 200번대 번호로 출력완료 메세지 리턴
        else:
            return Response(serializer.error, status=HTTP_400_BAD_REQUEST) #아닐경우 배드 리턴

