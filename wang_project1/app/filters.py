# 导入包
import django_filters
# 从3.6.4的rest_framework中导入 filters
from rest_framework import filters

from app.models import Student


# 定义一个类过滤继承自django_filters的FilterSet基类
class StudentFilter(filters.FilterSet):

    # 过滤查询的名字为模糊查询
    s_name = django_filters.CharFilter('s_name', lookup_expr='contains')
    s_chinese = django_filters.NumberFilter('s_chinese', lookup_expr='gte')
    s_math = django_filters.NumberFilter('s_math', lookup_expr='lt')

    # 指定源数据类
    class Meta:
        # 指定模型
        model = Student
        # 指定字段
        fields = ['s_name', ]
