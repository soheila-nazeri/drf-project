from typing import Any, Optional
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Article
from django.shortcuts import get_object_or_404
# Create your views here.

class ArticleList(ListView):
    def get_queryset(self) :
        return Article.objects.filter(status=True)
    
    
class ArticleDetail(DetailView):
    def get_object(self):
       queryset = Article.objects.filter(status=True)
       return get_object_or_404(queryset, pk=self.kwargs.get("pk"))