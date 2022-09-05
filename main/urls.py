from django.urls import path
from .views import FacultyList, InstructorList, StudentList, CourseList, student_detail, StudentCourseList, CourseSelectionCouseList
app_name = 'main'

urlpatterns = [
    path('faculty/', FacultyList.as_view(), name='faculty-list'),
    path('instructor/', InstructorList.as_view(), name='instructor-list'),
    path('student/', StudentList.as_view(), name='student-list'),
    path('student/<slug:username>/',
         StudentCourseList.as_view(), name='student_course_list'),
    path('course/', CourseList.as_view(), name='course-list'),
    path('courseselection/courselist/', CourseSelectionCouseList.as_view(),
         name='course-selection-courselist')
]
