from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template import RequestContext
import json
import time, re


def user_page(request):
    """打开登录页面"""
    data = {}

    # 得到跳转进来的页面
    referrer = request.META.get('HTTP_REFERER', '/')
    data['reback_url'] = referrer

    return render_to_response("user/user_page.html", data, )

# 检查登陆
def check_is_login(request):
    pass

# 登陆
def user_login(request):
    """"login"""
    response_data = {}

    try:
        login_name = request.POST.get('user_name')
        login_pwd = request.POST.get('user_pwd')

        if len(login_name)*len(login_pwd) == 0:
            raise Exception(u'邮箱或者密码为空')

        # 验证用户信息是否正确
        user = authenticate(username=login_name, password=login_pwd)
        if user is not None:
            login(request, user)
        else:
            raise Exception(u'邮箱或者密码不正确')

        response_data['sucess'] = True
        response_data['message'] = 'ok'
    except Exception as e:
        response_data['sucess'] = False
        response_data['message'] = e.message
    finally:
        # 返回json数据
        return HttpResponse(json.dumps(response_data), content_type='application/json')

# 登出
def user_logout(request):
    logout(request)
    # 记住原来的url，如果没有就设置为首页（'/'）
    returnPath = request.META.get('HTTP_REFERER', '/')
    # 重定向到原先页面
    return HttpResponseRedirect(returnPath)

# 注册
def user_register(request):
    response_data = {}
    register_name = ''

    try:
        register_name = request.POST.get('user_name')
        register_pwd = request.POST.get('user_pwd')

        # 验证交由前端处理
        # if  len(register_name)*len(register_pwd) == 0:
        #     raise Exception(u'邮箱或密码为空')
        #
        # # 匹配邮箱格式
        # pattern = re.compile(r'^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$')
        # match = pattern.match(register_name)
        # if not match:
        #     raise Exception(u'邮箱格式不正确')
        #
        # # 验证密码长度
        # if len(register_pwd)<6:
        #     raise Exception(u'密码不能少于6位')

        # 判断用户是否存在
        user = User.Object.filter(username=register_name)
        if len(user)>0:
            raise Exception(u'该用户已经被注册')

        # 创建新用户
        user = User(username= register_name, email=register_name)
        user.set_password(register_pwd) # 对密码加密
        # user.is_active=False
        user.save()

        response_data['success'] = True
        response_data['message'] = u'注册成功，并发送激活邮件到您的邮箱。'
    except Exception as e:
        response_data['sucess'] = False
        response_data['message'] = e.message
    finally:
        if response_data['sucess']:
            try:
                # 发送激活邮件
                pass
            except Exception as e:
                response_data['message'] = u'注册成功,激活邮件发送失败，请稍后重试'+e.message

            # 注册成功并登录
            user = authenticate(username=register_name, password=register_pwd)
            if user is not None:
                login(request, user)

        return HttpResponse(json.dumps(response_data), content_type='application/json')

#  忘记密码
def password_lost(request):
    pass


