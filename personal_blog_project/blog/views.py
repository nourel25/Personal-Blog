from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.views.generic import (
    ListView, 
    DetailView,
)



class ArticleListView(ListView):
    model = Article
    template_name = 'blog/home.html'
    context_object_name = 'articles'

class ArticelDetailView(DetailView):
    model = Article

# Admin Views
class DashBoard(UserPassesTestMixin, ListView):
    model = Article
    template_name = 'blog/dashboard.html'
    context_object_name = 'articles'

    def test_func(self):
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
        messages.error(self.request, 
                       "You do not have permission to view this page.")
        
        return redirect('home')
