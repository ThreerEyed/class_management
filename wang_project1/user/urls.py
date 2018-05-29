
from django.conf.urls import url
from user import views

# 注册
urlpatterns = [
    url(r'^djregister/', views.djregister, name='djregister'),
    url(r'^djlogin/', views.djlogin, name='djlogin'),
    url(r'^djlogout', views.djlogout, name='djlogout'),

    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout')
]