from django.urls import path
from .views import (
     home_view, LoginUser, PostCreateView, PostListView, profile_view, RegisterUser,
     PostDetailView,PostUpdateView
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('', home_view, name='home'),
    path('profile/',profile_view,name='profile'),
    path('post/create/',PostCreateView.as_view(),name="post-create"),
    path('posts/',PostListView.as_view(),name="posts"),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),

]
