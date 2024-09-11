from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/home.html'
    context_object_name = 'articles'

class ArticelDetailView(DetailView):
    model = Article