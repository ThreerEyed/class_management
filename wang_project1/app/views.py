from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponseRedirect, redirect

from django.core.urlresolvers import reverse

from app.models import Grade, Student
from wang_project1.settings import PAGE_NUMBERS


# def index(request):
#
#     if request.method == 'GET':
#
#         return render(request, 'index.html')


def head(request):

    if request.method == 'GET':

        return render(request, 'head.html')


def left(request):

    if request.method == 'GET':

        return render(request, 'left.html')


def grade(request):

    if request.method == 'GET':
        page_num = request.GET.get('page_num', 1)
        grades = Grade.objects.all()
        paginator = Paginator(grades, 3)
        pages = paginator.page(int(page_num))
        return render(request, 'grade.html', {'grades': grades, 'pages': pages})


# 编辑班级信息
def edit_grade(request):

    # 判断请求 是GET 就返回页面
    if request.method == 'GET':
        g_id = request.GET.get('g_id')
        g = Grade.objects.filter(id=g_id).first()
        ctx = {
            'g_name': g.g_name
        }
        return render(request, 'edit_grade.html', context=ctx)

    # 是post 就修改页面
    if request.method == 'POST':
        g_id = request.GET.get('g_id')
        g_name = request.POST.get('grade_name')
        Grade.objects.filter(id=g_id).update(g_name=g_name)
    return redirect('app:grade')


def addgrade(request):

    if request.method == 'GET':

        # g = Grade.objects.get(g_name__contains=grade)
        # g.save()
        return render(request, 'addgrade.html')

    if request.method == 'POST':
        """创建班级信息"""
        g_name = request.POST.get('grade_name')
        g = Grade()
        g.g_name = g_name
        g.save()
        # reverse 这个参数 可以使用命名空间的名字
        return HttpResponseRedirect(reverse('app:grade'))


def changepwd(request):

    if request.method == 'GET':

        return render(request, 'changepwd.html')


def main(request):

    if request.method == 'GET':

        return render(request, 'main.html')


def addstu(request):

    if request.method == 'GET':
        grades = Grade.objects.all()

        return render(request, 'addstu.html', {'grades': grades})

    if request.method == 'POST':

        s_name = request.POST.get('s_name')
        g_id = request.POST.get('g_id')

        s_img = request.FILES.get('s_img')

        grade = Grade.objects.filter(id=g_id).first()
        # 获取第一个 和get的区别是get一定要有这个对象 否则会报错, 获取到多个也会报错

        # 创建学生信息
        # Student.objects.create(s_name=s_name, g_id=grade.id)
        Student.objects.create(s_name=s_name, g=grade, s_img=s_img)

        return HttpResponseRedirect(reverse('app:student'))


# 学生信息展示
def student(request):

    if request.method == 'GET':
        page_num = request.GET.get('page_num', 1)
        stus = Student.objects.all()
        paginator = Paginator(stus, PAGE_NUMBERS)
        pages = paginator.page(int(page_num))

        return render(request, 'student.html', {'stus': stus, 'pages': pages})


# 删除学生信息
def del_student(request):
    s_id = request.GET.get('s_id')
    Student.objects.filter(id=s_id).delete()
    return redirect('app:student')


def head2(request):

    if request.method == 'GET':

        return render(request, 'head2.html')


"""
首页
"""


def index(request):

    if request.method == 'GET':

        return render(request, 'index.html')


