from django.urls import path
from .views import (EbookListCreateAPIView, EbookDetailAPIView, ReviewCreateAPIView,
                    ReviewDetailAPIView)

urlpatterns = [
    path('ebooks/', EbookListCreateAPIView.as_view(), name= "ebook-list"),
    path('ebooks/<int:pk>/', EbookDetailAPIView.as_view(), name= "ebook-detail"),
    path('ebooks/<int:ebook_pk>/reviews', ReviewCreateAPIView.as_view(), name="reviews-list"),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view(), name="reviews-detail")
]