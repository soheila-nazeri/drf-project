from rest_framework.generics import ListAPIView,ListCreateAPIView
from rest_framework.generics import RetrieveAPIView,DestroyAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from blog.models import Article
from .serializers import ArticleSerializer
# Create your views here.

class  ArticleList(ListAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    
    
class  ArticleListCreate(ListCreateAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    
class  ArticleRetrieveApiView(RetrieveAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    
class  ArticleDestroyApiView(DestroyAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    
#==============================    
class  ArticleRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    

class  ArticleRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    
class  ArticleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer