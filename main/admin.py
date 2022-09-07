from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import (Faculty, Major, Student, Instructor, MajorInstructor,
                     MajorCourse, Course, InstructorCourse, Section, CourseSelection, Semester)
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "email", "first_name", "last_name"),
            },
        ),
    )


class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name', 'manager', 'established_year']
    list_filter = ['established_year']
    search_fields = ['name', 'manager', 'established_year']
    ordering = ['name', ]


class MajorAdmin(admin.ModelAdmin):
    list_display = ['name', 'area_of_interest', 'code', 'grade', 'faculty']
    list_filter = ['name', 'area_of_interest']
    search_fields = ['name', 'area_of_interest']
    ordering = ['name']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['get_first_name', 'get_last_name', 'national_id', 'major']
    list_filter = ['major']
    list_select_related = ['user']
    search_fields = ['first_name', 'last_name']
    ordering = ['user__first_name', 'user__last_name', 'major']


class MajorInstructorAdmin(admin.ModelAdmin):
    list_display = ['major', 'instructor']
    list_filter = ['major', 'instructor']
    search_fields = ['instructor']
    ordering = ['instructor', 'major']


class InstructorAdmin(admin.ModelAdmin):
    list_display = ['get_first_name', 'get_last_name',
                    'national_id', 'get_majors', 'get_courses']

    list_select_related = ['user']

    list_filter = ['user__first_name', 'user__last_name']
    # , 'major', 'course']
    search_fields = ['user__first_name', 'user__last_name']
    ordering = ['user__first_name', 'user__last_name']


class InstructorCourseAdmin(admin.ModelAdmin):
    list_display = ['course', 'instructor', ]
    list_filter = ['instructor', 'course']
    search_fields = ['instructor']
    ordering = ['course', 'instructor']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'credit', 'get_majors', 'get_prerequisite']


class MajorCourseAdmin(admin.ModelAdmin):
    list_display = ['major', 'course']
    list_filter = ['major', 'course']
    search_fields = ['major', 'course']
    ordering = ['major', 'course']


class SectionAdmin(admin.ModelAdmin):
    list_display = ['course', 'instructor', 'class_time']
    list_filter = ['class_time', 'course', 'instructor']
    search_fields = ['class_time', 'course', 'instructor']
    ordering = ['course', 'instructor', 'class_time']


class CourseSelectionAdmin(admin.ModelAdmin):
    list_display = ['student', 'section']
    list_filter = ['student', 'section']
    search_fields = ['student', 'section']
    ordering = ['section', 'student']


class SemesterAdmin(admin.ModelAdmin):
    list_display = ['academic_year', 'semester']
    list_filter = ['academic_year', 'semester']
    search_fields = ['academic_year', 'semester']
    ordering = ['academic_year', 'semester']


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
admin.site.register(Semester, SemesterAdmin)
