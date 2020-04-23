from django.urls import path
from Jobs.api.views import (JobOfferCreateAPIView, JobOfferDetailAPIView)

urlpatterns = [
    path('jobs/', JobOfferCreateAPIView.as_view(), name="job_list"),
    path('jobs/<int:pk>', JobOfferDetailAPIView.as_view(), name="job_detail"),
]
