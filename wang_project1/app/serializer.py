
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
        model = Grade
        fields = ['id', 'g_name', 'g_create_time']

    def to_representation(self, instance):
        data = super().to_representation(instance)

        return data

