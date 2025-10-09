from django.urls import path
from .views import (
     home_view, LoginUser, PostCreateView, PostListView, profile_view, RegisterUser,
     PostDetailView,PostUpdateView,PostDeleteView,CommentUpdateView, CommentDeleteView,
     landing_posts,CommentCreateView,PostByTagListView
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('', home_view, name='home'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/',profile_view,name='profile'),
    path('post/new/',PostCreateView.as_view(),name="post-create"),
    path('posts/',PostListView.as_view(),name="posts"),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('home/posts', landing_posts, name='landing_posts'),
    path('posts/tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag')

]
