"""czxblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from apps_project.user.views import check_is_login, user_login, user_logout, user_register

urlpatterns = [
    url(r'^check_is_login/$', check_is_login, name='check_is_login'),  # 检查登录
    url(r'^login/$', user_login, name='user_login'),  # 登录
    url(r'^logout/$', user_logout, name='user_logout'),  # 登出
    url(r'^register$', user_register, name='user_register')  # 注册
]
