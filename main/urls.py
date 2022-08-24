from django.urls import path
from .views import FacultyList, InstructorList, StudentList, CourseList
app_name = 'main'

urlpatterns = [
    path('faculty/', FacultyList.as_view(), name='faculty-list'),
    path('instructor/', InstructorList.as_view(), name='instructor-list'),
    path('student/', StudentList.as_view(), name='student-list'),
    path('course/', CourseList.as_view(), name='course-list'),
]
