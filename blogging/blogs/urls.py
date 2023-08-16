# appname/urls.py

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path("blogs/<int:blog>", views.blog_post, name="blog_post_list"),
    path("blogs/newblog", views.new_blog, name="add_new_blog"),
    path("blogs/categorized_blogs/<str:category>", views.categorized_blogs, name="categorized_blogs"),

    path('logout/', views.user_logout, name="logout"),
    path("blogs/process_button_click", views.process_button_click, name="process_button_click"),
    path('like_comment/<int:comment>/<int:blog>/', views.like_comment, name='like_comment'),
    path('dislike_comment/<int:comment>/<int:blog>/', views.dislike_comment, name='dislike_comment'),
    path('',views.register,name='registration_form'),
    path('login/',views.user_login,name='login'),
    re_path(r'^totp/create/$', views.TOTPCreateView.as_view(), name='totp-create'),
    re_path(r'^totp/login/(?P<token>[0-9]{6})/$', views.TOTPVerifyView.as_view(), name='totp-login'),


]
