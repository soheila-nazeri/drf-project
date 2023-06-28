
from django.urls import path,include
from .views import ArticleList,ArticleRetrieveApiView,ArticleDestroyApiView
# from .views import ArticleListCreate
from .views import ArticleRetrieveDestroyAPIView,ArticleRetrieveUpdateAPIView,ArticleRetrieveUpdateDestroyAPIView
from .views import UserList,UserRetrieveUpdateDestroyAPIView
from .views import ArticleListCreateslug,RevoeToken
app_name='api'
urlpatterns = [
    path('revoke/',RevoeToken.as_view(),name='revoke'),
    path('',ArticleList.as_view(),name='list'),
    # path('listCreate/',ArticleListCreate.as_view(),name='list-create'),
    # path('<int:pk>/',ArticleRetrieveApiView.as_view(),name='detail'),
    # path('articles/<slug:slug>/', ArticleListCreateslug.as_view(), name='detail'),

   
    # path('<int:pk>/',ArticleDestroyApiView.as_view(),name='article-desctroy'),
    # path('<int:pk>/',ArticleRetrieveDestroyAPIView.as_view(),name='article-retrieve-desctroy'),
    # path('<int:pk>/',ArticleRetrieveUpdateAPIView.as_view(),name='article-retrieve-update'),
    path('<int:pk>/',ArticleRetrieveUpdateDestroyAPIView.as_view(),name='article-retrieve-desctroy-desctroy'),
    
    
    
    path('users/',UserList.as_view(),name='user-list'),
    path('users/<int:pk>/',UserRetrieveUpdateDestroyAPIView.as_view(),name='user-detail'),
    


]
