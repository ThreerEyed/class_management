
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from app import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^head/', views.head, name='head'),
    url(r'^left/', views.left, name='left'),
    url(r'^grade/', views.grade, name='grade'),
    url(r'^addgrade/', views.addgrade, name='addgrade'),
    url(r'^addstu/', views.addstu, name='addstu'),
    url(r'^main/', views.main, name='main'),
    url(r'^changepwd/', views.changepwd, name='changepwd'),
    # url(r'^login/', views.login, name='login'),
    url(r'^student/', views.student, name='student'),
    url(r'head2/', views.head2, name='head2'),
    url(r'^delete/', views.del_student, name='del_student'),
    url(r'^edit_grade/', views.edit_grade, name='edit_grade'),

]
