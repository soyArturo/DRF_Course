from django.urls import path
from news.api.views import (ArticleListCreateAPIView, ArticleDetailAPIView, JournalistCreateAPIView,
                            JournalistDetailAPIView)

urlpatterns = [
    path('articles/', ArticleListCreateAPIView.as_view(), name="article_list"),
    path('articles/<int:pk>/', ArticleDetailAPIView.as_view(), name="article_detail"),
    path('journalists/', JournalistCreateAPIView.as_view(), name="journalist_list"),
    path('journalists/<int:pk>/', JournalistDetailAPIView.as_view(), name="journalist_detail"),
]
