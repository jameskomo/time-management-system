from django.urls import path
from django.conf.urls import url
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView, 
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='timeapp-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='timeapp-about'),
    url(r'^searchpost/$', views.postsearch, name='post-search'),
]
