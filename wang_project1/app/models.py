from django.db import models


class Grade(models.Model):
    g_name = models.CharField(max_length=20)
    g_create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'grade'


class Student(models.Model):

    g = models.ForeignKey(Grade)
    s_name = models.CharField(max_length=20, null=False, unique=True)
    s_create_time = models.DateTimeField(auto_now_add=True)
    s_operate_time = models.DateTimeField(auto_now=True)
    s_img = models.ImageField(upload_to='upload', null=True)
    s_chinese = models.IntegerField(null=True)
    s_math = models.IntegerField(null=True)
    stu_tel = models.CharField(max_length=11, null=True)
    stu_birth = models.DateField(null=True)
    stu_delete = models.BooleanField(default=0)
    stu_sex = models.BooleanField(default=0, null=True)

    class Meta:
        db_table = 'student'
        # ordering = ('id',)


class StuInfo(models.Model):

    stu_addr = models.CharField(max_length=30)
    stu_age = models.IntegerField()
    stu = models.OneToOneField(Student)

    class Meta:
        db_table = 'stu_info'




