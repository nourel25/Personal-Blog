from django.urls import path
from .views import (
    ArticleListView, 
    ArticelDetailView,
    DashBoard
)

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    path('article/<int:pk>/', ArticelDetailView.as_view(), name='article-detail'),
    path('dashboard/', DashBoard.as_view(), name='dashboard')
]