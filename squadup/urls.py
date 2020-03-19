from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('comments/', views.CommentList.as_view(), name='comment_list'),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('posts/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name='comment_detail')
]
