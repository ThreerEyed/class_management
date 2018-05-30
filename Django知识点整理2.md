---
title: Django知识点整理2
date: 2018-05-29 19:21:00
categories: Django
tags: [Django, 中间件, 登录验证, 上传媒体文件]
---



### Django 知识点整理 



#### 媒体文件上传

在使用 django 做web开发的时候,  我们经常会需要上传一些文件之类的,  最常见的就是图片了,  比如我们需要上传自己的个人信息蓝白底一寸彩照这种.  

1. 在表单中做添加图片的时候需要将 Form 的属性做一下设置

```django
<form action="" method="post" enctype="multipart/form-data">
{% csrf_token %}  # cross site request forgery  
```



2. 上传文件的标签属性设置

```django
<input type="file" name="s_img">
```

3. 修改模型,  添加字段 

```python
s_img = models.ImageField(upload_to='upload', null=True)
```

4. 后面参数 upload_to 是上传的文件位置



5. 修改配置文件 settings 

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

6. 在项目同级目录下添加一个 media 文件夹
7. 最后

```django
<td><img src="/media/{{ page.s_img }}" width="100px" height="70px" alt="头像"/></td>
```





#### 登录 注册

使用django做web开发的时候,  虽然django为我们提供了一个后台管理,   但是我们一般在开发中不使用这个登录,   而是自己做一个登录和注册的功能. 

#### 1. 创建Users模型

我们需要自己写一个  user应用 用于处理登录和注册的相关信息

```python
from django.db import models


class Users(models.Model):

    username = models.CharField(max_length=10)
    password = models.CharField(max_length=200)
    ticket = models.CharField(max_length=30)
    create_time = models.DateTimeField(auto_now_add=True)   # 创建的时间, 以后不会修改
    login_time = models.DateTimeField(auto_now=True)        # 登录的时间, 每一次登录都会有一个记录

    class Meta:
        db_table = 'user'   # 定义在数据库中显示的表名
```

自己做得好处是可以任意的添加修改和删除,   相关的字段也便于管理  写好模型之后就生成迁移再迁移到数据库中去.  





#### 2. 中间件过滤URL request

多个页面访问的时候,  如果没有登录那肯定是不能访问的,  所以我们要做一个事情,   那就是所有相关的请求, 我们都需要将他们过滤,   所以这个时候 我们就需要中间件这个东西了

- 添加一个文件夹

![1](django知识点整理2/1.png)



- 修改配置文件

![2](django知识点整理2/2.png)





- 添加文件

```python
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from user.models import Users


# 定义中间件这个类 继承自  MiddlewareMixin
class UserAuthMiddle(MiddlewareMixin):
	
    # 定义这个中间件方法, 参数为request请求
    def process_request(self, request):

        # 验证cookie中的ticket, 验证不通过, 跳转到登录
        # 验证通过1, request, user当前登录的用户信息
        # return None 或者不写return

        # 拿到这个路径并做判断, 如果在这个列表中就不做处理或返回None
        path = request.path
        s = ['/user/login/', '/user/register/']
        if path in s:
            return None

        # 将这个url的Cookies中的 ticket 取出来
        ticket = request.COOKIES.get('ticket')

        # 如果没有 则重定向到登录界面
        if not ticket:
            return HttpResponseRedirect(reverse('user:login'))
        
        # 有就拿到user对象
        user = Users.objects.filter(ticket=ticket)
        if not user:
            return HttpResponseRedirect(reverse('user:login'))

        # 将这个user赋值给request对象的user
        request.user = user
```



#### 3. 注册

```python
def register(request):
	
    # 判断请求 如果是GET就直接渲染页面即可
    if request.method == 'GET':
        return render(request, 'register.html')
	# 如果是POST请求
    if request.method == 'POST':

      	# 拿到相关页面的name属性 
        username = request.POST.get('username')
        pwd1 = request.POST.get('pwd1')
        pwd2 = request.POST.get('pwd2')
		
        # 做一个all 判断是否为空, all中的参数是一个可迭代对象
        if not all([username, pwd2, pwd1]):
            msg = '信息不能为空'
            return render(request, 'register.html', {'msg': msg}) # 带参数渲染页面

        if pwd1 != pwd2:
            msg = '密码输入不一致'
            return render(request, 'register.html', {'msg': msg})
		
        # 创建一个user对象
        Users.objects.create(username=username, password=pwd1)

        # 重定向
        return redirect(reverse('user:login'))
```



#### 4. 登录

```python
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
		
        # 拿到数据库中的user对象
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
            
            # 拿到响应之后, 给cookie的ticket设置一个生成好的ticket
            response.set_cookie('ticket', ticket)
			
            # 再返回这个响应
            return response
```



