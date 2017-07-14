from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
import json

# 检查登陆
def check_is_login(request):
    pass

# 登陆
def user_login(request):
    """"login"""
    response_data = {}

    try:
        login_name = request.POST.get('login_name')
        login_pwd = request.POST.get('login_pwd')

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
        register_name = request.POST.get('register_name')
        register_pwd = request.POST.get('register_pwd')

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





