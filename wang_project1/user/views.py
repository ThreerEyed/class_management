import random

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth


# 注册信息
from django.core.urlresolvers import reverse

from user.models import Users, Role, Permission


def djregister(request):

    if request.method == 'GET':

        return render(request, 'register.html')

    if request.method == 'POST':

        username = request.POST.get('username')
        pwd1 = request.POST.get('pwd1')
        pwd2 = request.POST.get('pwd2')

        if not all([username, pwd1, pwd2]):
            msg = '请填写玩所有参数'
            return render(request, 'register.html', {'msg':msg})

        if pwd1 != pwd2:
            msg = '密码不一致'
            return render(request, 'register.html', {'msg': msg})

        User.objects.create_user(username=username, password=pwd1)

        return redirect(reverse('app:login'))


# 登录信息
def djlogin(request):

    if request.method == 'GET':

        return render(request, 'login.html')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        # 返回验证成功的用户信息
        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            return redirect(reverse('app:index'))
        else:
            msg = '用户名或者密码错误'
            return render(request, 'login.html', {'msg': msg})


def djlogout(request):

    if request.method == 'GET':
        auth.logout(request)

    return redirect(reverse('login.html'))


"""
登录注册 自己实现
"""


def register(request):

    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':

        username = request.POST.get('username')
        pwd1 = request.POST.get('pwd1')
        pwd2 = request.POST.get('pwd2')

        if not all([username, pwd2, pwd1]):
            msg = '信息不能为空'
            return render(request, 'register.html', {'msg': msg})

        
        if pwd1 != pwd2:
            msg = '密码输入不一致'
            return render(request, 'register.html', {'msg': msg})

        Users.objects.create(username=username, password=pwd1)

        return redirect(reverse('user:login'))


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = Users.objects.filter(username=username, password=password).first()
        if user:
            s = 'qwertyuiopasdfghjklzxcvbnm1234567890'
            # HttpResponseRedirect()
            # 先产生随机的字符串  长度28
            # 保存在服务端
            # 保存在客户端 中的cookies
            ticket = ''
            for i in range(28):
                ticket += random.choice(s)
            user.ticket = ticket
            user.save()
            response = HttpResponseRedirect(reverse('app:index'))
            response.set_cookie('ticket', ticket)

            return response

        return HttpResponseRedirect(reverse('user:login'))


"""登出"""


def logout(request):
    if request.method == 'GET':
        response = HttpResponseRedirect(reverse('user:login'))
        response.delete_cookie('ticket')

        return response


def userper(reqeust):

    # 查询小英有哪些权限

    user = Users.objects.filter(username='小英').first()

    # 通过user对象 查到他的角色, 然后通过角色查到权限
    # 一对一可以直接使用 user.role 反查到对应的角色
    per = user.role.r_p.all()
    role = Role.objects.filter(u_id=user.id).first()
    # per = Permission.objects.filter(id=role.id)
    # 判断用户是否有学生列表的权限

    # a = Permission.objects.filter(id=3).first()
    # if a in per:
    #     return HttpResponse('有')
    # else:
    #     return HttpResponse('没有')


