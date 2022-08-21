from django.contrib import admin
from .models import (Faculty, Major, Student, Instructor, MajorInstructor,
                     MajorCourse, Course, InstructorCourse, Section, CourseSelection)


class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name', 'manager', 'established_year']
    list_filter = ['established_year']
    search_fields = ['name', 'manager', 'established_year']
    ordering = ['-name']


class MajorAdmin(admin.ModelAdmin):
    list_display = ['name', 'area_of_interest', 'grade', 'faculty']
    list_filter = ['name', 'area_of_interest']
    search_fields = ['name', 'area_of_interest']
    ordering = ['-name']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'major']
    list_filter = ['first_name', 'last_name', 'major']
    search_fields = ['first_name', 'last_name']
    ordering = ['-first_name', '-last_name', '-major']


class MajorInstructorAdmin(admin.ModelAdmin):
    list_display = ['major', 'instructor']
    list_filter = ['major', 'instructor']
    search_fields = ['instructor']
    ordering = ['-instructor', '-major']


class InstructorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'get_majors', 'get_courses']
    list_filter = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']  # , 'major', 'course']
    ordering = ['-first_name', '-last_name']


class InstructorCourseAdmin(admin.ModelAdmin):
    list_display = ['course', 'instructor', ]
    list_filter = ['instructor', 'course']
    search_fields = ['instructor']
    ordering = ['-course', '-instructor']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'credit', 'get_majors', 'get_prerequisite']


class MajorCourseAdmin(admin.ModelAdmin):
    list_display = ['major', 'course']
    list_filter = ['major', 'course']
    search_fields = ['major', 'course']
    ordering = ['-major', '-course']


class SectionAdmin(admin.ModelAdmin):
    list_display = ['course', 'instructor', 'class_time']
    list_filter = ['class_time', 'course', 'instructor']
    search_fields = ['class_time', 'course', 'instructor']
    ordering = ['-course', '-instructor', '-class_time']


class CourseSelectionAdmin(admin.ModelAdmin):
    list_display = ['student', 'section']
    list_filter = ['student', 'section']
    search_fields = ['student', 'section']
    ordering = ['-section', '-student']


# Register your models here.
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Major, MajorAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(MajorInstructor, MajorInstructorAdmin)
admin.site.register(InstructorCourse, InstructorCourseAdmin)
admin.site.register(MajorCourse, MajorCourseAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(CourseSelection, CourseSelectionAdmin)
