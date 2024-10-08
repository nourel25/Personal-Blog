from django.urls import path
from .views import (
    ArticleListView, 
    ArticelDetailView,
    DashBoard,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView
)

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    path('article/<int:pk>/', ArticelDetailView.as_view(), name='detail'),
    path('dashboard/', DashBoard.as_view(), name='dashboard'),
    path('article/new/', ArticleCreateView.as_view(), name='new'),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name='update'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='delete'),
]