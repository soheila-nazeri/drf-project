from rest_framework import serializers
from blog.models import Article
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        # fields=('title','slug','author','content','publish','status' )
        # or exclude
        exclude=('created','updated')
        #or all data
        # fields="__all__"
        
