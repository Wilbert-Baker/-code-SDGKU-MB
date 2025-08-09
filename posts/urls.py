from django.urls import path
from .views import (
    postlistView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlspattern = [
    path('',PostListView.as_View(), name="post_list"),
    path('<int:pk>/', postDetailView.as_view(), name="post_detail"),
    path('new/', PostCreateView.as_view(), name="post_new"),
    path(<'int:pk>/edit/', PostUpdate.as_view(), name="post_edit"),
    path('<int:pk/delete/', PostDeleteView.as_view(), name"post_delete"),
]