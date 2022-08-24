from django.views.generic import ListView
from .models import (Faculty, Instructor, Student, Course, Major,
                     MajorInstructor, InstructorCourse, MajorCourse, Section, CourseSelection)
# Create your views here.


class FacultyList(ListView):
    queryset = Faculty.objects.all()
    template_name = 'list_view.html'


class InstructorList(ListView):
    queryset = Instructor.objects.all()
    template_name = 'list_view.html'


class StudentList(ListView):
    queryset = Student.objects.all()
    template_name = 'list_view.html'


class CourseList(ListView):
    queryset = Course.objects.all()
    template_name = 'list_view.html'


class MajorInstructorList(ListView):
    queryset = MajorInstructor.objects.all()
    template_name = 'list_view.html'


class InstructorCourseList(ListView):
    queryset = InstructorCourse.objects.all()
    template_name = 'list_view.html'


class MajorCourseList(ListView):
    queryset = MajorCourse.objects.all()
    template_name = 'list_view.html'


class SectionList(ListView):
    queryset = Section.objects.all()
    template_name = 'list_view.html'


class CourseSelectionList(ListView):
    queryset = CourseSelection.objects.all()
    template_name = 'list_view.html'