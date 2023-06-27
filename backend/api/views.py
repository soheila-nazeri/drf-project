from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.generics import (
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAdminUser
from blog.models import Article
from .serializers import ArticleSerializer, UserSerializer
from .permissions import (
    IsSuperUser,
    IsAuthorOrReadonly,
    IsStaffOrReadOnly,
    IsSuperUserOrStaffReadonly)

# Create your views here.


class ArticleList(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleListCreate(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    

class ArticleListCreateslug(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'

    
    

class ArticleRetrieveApiView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDestroyApiView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


# ==============================
class ArticleRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes=(IsAuthorOrReadonly ,IsStaffOrReadOnly)


# ================================== users
# ===list
class UserList(ListCreateAPIView):
    # permission_classes=(IsAdminUser,)
    # permission_classes=(IsSuperUser,IsStaffOrReadOnly)
    permission_classes=(IsSuperUserOrStaffReadonly,)
    
    queryset = User.objects.all()
    serializer_class = UserSerializer


# ===detail
class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    # permission_classes=(IsAdminUser,)
    # permission_classes=(IsSuperUser,)
    permission_classes=(IsSuperUserOrStaffReadonly,)
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
