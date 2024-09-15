from django.shortcuts import redirect
from .models import Article
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
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


class ArticleCreateView(UserPassesTestMixin, CreateView):
    model = Article
    fields = ['title', 'content']

    def test_func(self):
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
        messages.error(self.request, 
                       "You do not have permission to view this page.")
        
        return redirect('home')
    
    def form_valid(self, form):
        messages.success(self.request, "Article created successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('dashboard')
    

class ArticleUpdateView(UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['title', 'content']

    def test_func(self):
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
        messages.error(self.request, 
                       "You do not have permission to view this page.")
        
        return redirect('home')
    
    def form_valid(self, form):
        messages.success(self.request, "Article updated successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('dashboard')
    

class ArticleDeleteView(UserPassesTestMixin, DeleteView):
    model = Article

    def test_func(self):
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
        messages.error(self.request, 
                       "You do not have permission to view this page.")
        
        return redirect('home')

    def get_success_url(self):
        return reverse('dashboard')