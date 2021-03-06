from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from .views import (
    CategoryListView, 
    CategoryCreateView,
    TopicListView1, 
    TopicListView2, 
    ThreadListView,
    ThreadCreateView, 
    PostListView, 
    TopicCreateView,
    PostCreateView,
    PostDeleteView,
    TopicDeleteView,
    ThreadDeleteView,
    CategoryDeleteView,
    CategoryUpdateView,
    ThreadUpdateView,
    TopicUpdateView,
    PostUpdateView,
)

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='admin_login.html'), name='admin_login'),
    path('', CategoryListView.as_view(), name='admin_home'),
    path('categorys/create/', CategoryCreateView.as_view(), name='category_create'),
    path('threads/', ThreadListView.as_view(), name='admin_threads'),
    path('threads/create/', ThreadCreateView.as_view(), name='thread_create'),
    path('topics1/', TopicListView1.as_view(), name='admin_topics1'),
    path('topics2/', TopicListView2.as_view(), name='admin_topics2'),
    path('topics/create/', TopicCreateView.as_view(), name='topic_create'),
    path('posts/create', PostCreateView.as_view(), name='post_create'),
    path('posts/', PostListView.as_view(), name='admin_posts'),
    re_path(r'^posts/(?P<pk>\d+)/delete/$', PostDeleteView.as_view(), name='delete_post'),
    re_path(r'^topics/(?P<pk>\d+)/delete/$', TopicDeleteView.as_view(), name='delete_topic'),
    re_path(r'^threads/(?P<pk>\d+)/delete/$', ThreadDeleteView.as_view(), name='delete_thread'),
    re_path(r'^category/(?P<pk>\d+)/delete/$', CategoryDeleteView.as_view(), name='delete_category'),
    re_path(r'^posts/(?P<pk>\d+)/update/$', PostUpdateView.as_view(), name='update_post'),
    re_path(r'^topics/(?P<pk>\d+)/update/$', TopicUpdateView.as_view(), name='update_topic'),
    re_path(r'^threads/(?P<pk>\d+)/update/$', ThreadUpdateView.as_view(), name='update_thread'),
    re_path(r'^category/(?P<pk>\d+)/update/$', CategoryUpdateView.as_view(), name='update_category'),
]