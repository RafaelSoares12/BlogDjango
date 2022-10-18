from django.contrib import admin
from django.urls import path
from .views import HomeView, ArticleDetailView 

urlpatterns = [
    path('', HomeView.as_view(), name="index"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="readMore")
]
