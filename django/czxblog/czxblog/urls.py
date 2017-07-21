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
from django.conf.urls import url, include
from django.contrib import admin
from apps_project.blog.views import index


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),  # 主页
    url(r'^ueditor/', include('apps_project.ueditor.urls')),  # 百度编辑器
    url(r'^blog/', include('apps_project.blog.urls')),  # 博客
    url(r'^user/', include('apps_project.user.urls')),  # 用户
]
