"""djangoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from blog import views

urlpatterns = [
    # 用户管理
    path('login/', views.login),  # 登录
    path('register/', views.register),  # 注册
    path('logout/', views.logout),  # 登出
    path('uniqueness/', views.uniqueness),   # 提前验证邮箱与用户名唯一性
    path('changepassword/', views.change_password),  # 修改密码
    # 文章管理
    path('add-article/', views.add_article),  # 添加文章
    path('article/', views.article_data),  # 文章详情
    path('article-list/', views.article_list),  # 文章列表
    path('category/', views.category),  # 分类
    path('tag/', views.tag),  # 标签
    path('like/', views.like),      # 点赞
    path('collection/', views.collection),   # 收藏
    path('comment/', views.comment),  # 评论
]
