---
title: Django知识点整理3
date: 2018-05-30 08:49:07
categories:
tags:
---



### Django知识点整理3





### 使用装饰器来代替中间件验证登录

```python
def is_login(func):
    def check_login(request):
        
        ticket = request.COOKIES.get('ticket')
        
        if not ticket:
            
            return HttpRessponseRedirect(reverse('user:login'))
        
        user = User.objects.filter(ticket=ticket)
        
        if not user:
            
            return HttpRessponseRedirect(reverse('user:login'))
        
        return func
    
    return check_login
```







### 模板继承的继承与导入: 



　　__情况1__：通常写页面都有个模板用来框定头部LOGO页面，左侧导航菜单，只有右部的内容不同。如果不使用模板就大量重复工作。

　　　　　　特别如果头部或者左侧导航需要修改或者添加，所有页面都需要修改。django 通过模板继承解决。

　　__情况2__：一个页面如果内容特别多，不可能都一起写同一个页面。比如京东首页内容非常多。django通过include导入其他页面。

 

#### 一：模版继承

**步骤1：母板里写入block，就可以被继承，content是名称**　

这里 **indexbody** 和 **content** 的区别是,   indexbody 可以不要body标签,   但是  content 是写在body 标签里面的

```django
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>
        {% block title %}
        {% endblock %}
    </title>
    {% block meta %}
    {% endblock %}
    {% block extCSS %}
    {% endblock %}
    {% block extJS %}
    {% endblock %}
</head>
    {% block indexbody %}
    {% endblock %}
<body>
    {% block content %}
    {% endblock %}

    {% block footer %}
    {% endblock %}
</body>
</html>
```

**步骤2：子页面通过extends指定继承那个模板**



```django
  
{% extends 'base.html' %}
{% block title %}
    登录
{% endblock %}
{% block extCSS %}
<link rel="stylesheet" type="text/css" href="/static/css/public.css" />
<link rel="stylesheet" type="text/css" href="/static/css/page.css" />
{% endblock %}
{% block extJS %}
<script type="text/javascript" src="/static/js/jquery.min.js"></script>
<script type="text/javascript" src="/static/js/public.js"></script>
{% endblock %}


{% block indexbody %}
<form action="" method="post">
    {% csrf_token %}
	<!-- 登录body -->
	<div class="logDiv">
		<img class="logBanner" src="/static/img/logBanner.png" />
		<div class="logGet">
			<!-- 头部提示信息 -->
			<div class="logD logDtip">
				<p class="p1">登录</p>
			</div>
			<!-- 输入框 -->
			<div class="lgD">
				<img class="img1" src="/static/img/logName.png" /><input type="text"
					placeholder="输入用户名" name="username" />
			</div>
			<div class="lgD">
				<img class="img1" src="/static/img/logPwd.png" /><input type="password"
					placeholder="输入用户密码" name="password" />
			</div>
			<div class="logC">
                <button>
                    <input type="submit" value="登 录"/>
                </button>
			</div>
		</div>
	</div>
    </form>
	<!-- 登录body  end -->

	<!-- 登录页面底部 -->
	<div class="logFoot">
		<p class="p1">版权所有：安徽公司公司</p>
		<p class="p2">123456789</p>
	</div>
	<!-- 登录页面底部end -->
{% endblock %}
```



​    **如果子页面有自己的css,js 怎么用了？**
　　如果是在子页面写CSS和JS，CSS就不是在头部了，而JS也不是在<body>之前，假如要引用jquery,子页面写的JS会在jquery引用前面，就会不生效

　　继承CSS与JS都是共有的。

　　**解决方法：**

　　**在模板里css 和js位置在写个block块。然后在block里引入，在这个block写自己的js和css**
        注：block和顺序没有关系



#### 二:模板引入使用

　　**一个页面只能继承一个模板，如何使用多个模板，或者引入其他页面**

　　　　`<% include "a.html" %>` 可以引用多次

　　**模板，include，子页面怎么渲染？**
        先把自己渲染成字符串，在拿模板和include渲染，所以不存在渲染问题(可以把子页面继承include当做一个整页面)







### 查询 : 



#### F ()  和 Q() 的使用

#### 1. F()

```python
django支持对F()对象使用算数运算 

   list.filter(bread__gte=F(‘bcommit’)*2)

F()对象中还可以写作”模型类__列名”进行关联查询 

   list.filter(isDelete=F(‘heroinfo__isDelete’))

对于date/time字段，可与timedelta()进行运算 

   list.filter(bpub_date__lt=F(‘bpub_date’)+timedelta(days=1))

```



#### 2. Q()

作用：对对象进行复杂查询，并支持&（and）,|（or），~（not）操作符。

基本使用：

```python
from django.db.models import Q
search_obj=Asset.objects.filter(Q(hostname__icontains=keyword)|Q(ip=keyword))
```

如果查询使用中带有关键字查询，Q对象一定要放在前面

```python
Asset.objects.get(
Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)),
question__startswith='Who')
```

通过模型创建数据 ,  然后通过  rom  来查询我们需要的数据

```python
创建班级的模型
class Grade(models.Model):
    g_name = models.CharField(max_length=20)
    g_create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'grade'

创建学生的模型：
    class Student(models.Model):
        stu_name = models.CharField(max_length=6, unique=True)
        stu_sex = models.BooleanField(default=0)
        stu_birth = models.DateField()
        stu_delete = models.BooleanField(default=0)
        stu_create_time = models.DateField(auto_now_add=True)
        stu_operate_time = models.DateField(auto_now=True)
        stu_tel = models.CharField(max_length=11)
        stu_yuwen = models.DecimalField(max_digits=3, decimal_places=1, default=0)
        stu_shuxue = models.DecimalField(max_digits=3, decimal_places=1, default=0)
        g = models.ForeignKey(Grade)

        class Meta:
            db_table = 'stu'

创建学生拓展的模型：		
    class StuInfo(models.Model):

        stu_addr = models.CharField(max_length=30)
        stu_age = models.IntegerField()
        stu = models.OneToOneField(Student)

        class Meta:
            db_table = 'stu_info'


#1. 通过某个学生拓展表去获取学生信息
stu = StuInfo.objects.filter(stu_age==?).first()


#2. 通过学生表获取个人拓展表的信息


#3. 获取python班下的所有学生的信息和拓展表的信息
grade = Grade.objects.filter(g_name == 'python')
grade.student_set.all()

#4. 获取python班下语文成绩大于80分的女学生
grade = Grade.objects.filter(g_name == 'python')
stu = grade.filter(Q(stu_yuwen__gt=80) & Q(stu_sex == 0))
stu.stu_name

#5. 获取python班下语文成绩超过数学成绩10分的男学生
grade = Grade.objects.filter(g_name == 'python')
stu = grade.filter(Q(stu_yuwen__gt=F('stu_shuxue') + 10) & Q(stu_sex == 1))

#6. 获取出生在80后的男学生，查看他们的班级
stu = StuInfo.objects.filter(Q(stu_age__gte=38) & Q(stu_sex == 1))
grade = stu.grade.all().first()
```

查询数据时 : 

一对多 :

- 多找一:    通过外键关联去找
  - student.g.g_name
  - student.g.id
- 一找多 :   通过   模型名_set   去找
  - grade.student_set.all()



一对一 :  反查通过外键关联去查找

- student.g.g_name
- grade.student.all()



### 用户权限 : 