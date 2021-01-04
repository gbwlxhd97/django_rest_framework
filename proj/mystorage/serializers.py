from .models import Essay,Album,Files
from rest_framework import serializers

class EssaySerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='author.username') #글을쓴 사용자명을 지정해줌. views.py 에서도 설정해주기.


    class Meta:
        model = Essay #레스트 프레임워크에서 Essay 활성화.
        fields = ('pk', 'title', 'body', 'author_name')


class AlbumSerializer(serializers.ModelSerializer):
     author_name = serializers.ReadOnlyField(source='author.username')
     image = serializers.ImageField(use_url=True) #이미지가 업로드됐는지 확인을 URL로 하겠다. ex:포스트로 업로드를하면, 127.0.0./media~~/imagae등등이렇게 url로 나옴

     class Meta:
        model = Album
        fields = ('pk','author_name','image','desc')

class FilesSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    myfile = serializers.FileField(use_url=True)

    class Meta:
        model = Files
        fields = ('pk','author_name', 'myfile', 'desc')


