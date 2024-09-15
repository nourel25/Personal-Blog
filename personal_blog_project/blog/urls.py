from django.urls import path
from .views import (
    ArticleListView, 
    ArticelDetailView,
    DashBoard,
    ArticleCreateView
)

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    path('article/<int:pk>/', ArticelDetailView.as_view(), name='article-detail'),
    path('dashboard/', DashBoard.as_view(), name='dashboard'),
    path('new/', ArticleCreateView.as_view(), name='new')
]