from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import (Faculty, Instructor, Student, Course, Major,
                     MajorInstructor, InstructorCourse, MajorCourse, Section, CourseSelection, User)
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


def student_detail(requset, username):
    student = User.objects.get(username=username)
    courses = CourseSelection.objects.all().filter(student_id=student.student.id)
    context = {'student': student, 'courses': courses}
    return render(requset, 'student-detail.html', context)


