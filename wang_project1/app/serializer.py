
from rest_framework import serializers

from app.models import Student, Grade


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['s_name', 's_chinese', 'g', ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['g_name'] = instance.g.g_name

        return data


class GradeSerializer(serializers.ModelSerializer):

    class Meta:
        # 指定模板
        model = Grade
        # 指定字段
        fields = ['id', 'g_name', 'g_create_time']

    # 序列化
    def to_representation(self, instance):
        data = super().to_representation(instance)

        return data



