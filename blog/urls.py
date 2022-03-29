from django.urls import path

from .views import CommentCreateview, PostDetailView, PostListView

urlpatterns = [
    path('feed/', PostListView.as_view()),
    path('feed/<int:pk>/', PostDetailView.as_view()),
    path('comment/', CommentCreateview.as_view()),
]