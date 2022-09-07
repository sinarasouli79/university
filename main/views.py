from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import (Faculty, Instructor, Student, Course, Major,
                     MajorInstructor, InstructorCourse, MajorCourse, Section, CourseSelection, User)

from django.contrib.auth.decorators import login_required
from .forms import CourseSelectionForm

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
    queryset = Section.objects.all()
    template_name = 'list_view.html'


def student_detail(requset, username):
    student = User.objects.get(username=username)
    courses = CourseSelection.objects.all().filter(student_id=student.student.id)
    context = {'student': student, 'courses': courses}
    return render(requset, 'student-detail.html', context)


class StudentCourseList(LoginRequiredMixin, ListView):
    template_name = 'student-courses-list.html'

    def get_queryset(self):
        global student
        student = User.objects.get(username=self.kwargs.get('username'))
        courses = CourseSelection.objects.all().filter(student_id=student.student.id)
        return courses

    def get_context_data(self, **kwargs):
        return super().get_context_data(**{'student_name': student.get_full_name})


class CourseSelectionCouseList(LoginRequiredMixin, ListView):
    model = Section
    template_name = 'course-selection-couseList.html'


@login_required
def course_selection(request, *args, **kwargs):
    form = CourseSelectionForm()
    if request.method == 'POST':
        form = CourseSelectionForm(request.POST)
        if form.is_valid():
            section_code_input = form.cleaned_data.get('section_code')
            print(section_code_input)
            course_code_input = form.cleaned_data.get('course_code')
            section = Section.objects.filter(
                course__code=course_code_input).filter(section_code_input).get()
            print(section)
            # student = request.user.student
            # print(student, section_code_input)
            # CourseSelection.objects.create(section=section, student=student)
            # form = StudentCourseSelection()

    return render(request, 'course_selection_form.html', {'form': form})
