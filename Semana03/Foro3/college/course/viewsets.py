
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from course.serializers import NewCourseSerializer
from course.models import Course


class NewCourseModelViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = NewCourseSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def perform_create(self, serializer):
    #     serializer.save()
