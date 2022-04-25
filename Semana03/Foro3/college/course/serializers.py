from rest_framework import serializers
from course.models import Course

class NewCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('title', 'description','created_at', 'updated_at', 'credits','category')
