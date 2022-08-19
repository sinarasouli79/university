from django.contrib import admin
from .models import (Faculty, Major, Student, Instructor, MajorInstructor,
                     MajorCourse, Course, InstructorCourse, Section, CourseSelection)
# Register your models here.
admin.site.register(Faculty)
admin.site.register(Major)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(MajorInstructor)
admin.site.register(MajorCourse)
admin.site.register(Course)
admin.site.register(InstructorCourse)
admin.site.register(Section)
admin.site.register(CourseSelection)
