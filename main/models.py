from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib import admin
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)


class Faculty(models.Model):
    name = models.CharField(max_length=30, verbose_name='نام', unique=True)
    manager = models.CharField(max_length=30, verbose_name='مدیر')
    established_year = models.DateField(verbose_name='سال تاسیس')

    class Meta:
        verbose_name = 'دانشکده'
        verbose_name_plural = 'دانشکده‌ها'

    def __str__(self) -> str:
        return self.name


class Major(models.Model):
    BACHELOR = 'B'
    MASTER = 'M'
    DOCTORATE = 'D'
    GRADE_CHOISES = [
        (BACHELOR, 'کارشناسی'),
        (MASTER, 'کارشناسی ارشد'),
        (DOCTORATE, 'دکترا'),
    ]
    name = models.CharField(max_length=100, verbose_name='نام')
    code = models.CharField(max_length=10, unique=True, verbose_name='کد درس')
    area_of_interest = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='گرایش')
    grade = models.CharField(
        max_length=1, choices=GRADE_CHOISES, default=BACHELOR, verbose_name='مقطع')
    faculty = models.ForeignKey(
        Faculty, on_delete=models.PROTECT, verbose_name='دانشکده')

    class Meta:
        verbose_name = 'رشته'
        verbose_name_plural = 'رشته‌ها'

    def __str__(self) -> str:
        return f'{self.name}-{self.area_of_interest}'


class Student(models.Model):
    national_id = models.CharField(
        max_length=10, unique=True, verbose_name='کدملی')
    major = models.ForeignKey(
        Major, on_delete=models.PROTECT, verbose_name='رشته')

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'دانشجو'
        verbose_name_plural = 'دانشجویان'

    def __str__(self) -> str:
        return f'{self.user.first_name}-{self.user.last_name}'

    @admin.display(ordering='user__first_name')
    def get_first_name(self):
        return self.user.first_name
    get_first_name.short_description = 'نام'

    @admin.display(ordering='user__last_name')
    def get_last_name(self):
        return self.user.last_name
    get_last_name.short_description = 'نام‌خانوادگی'


class MajorInstructor(models.Model):
    major = models.ForeignKey(
        Major, on_delete=models.PROTECT, verbose_name='رشته')
    instructor = models.ForeignKey(
        'Instructor', on_delete=models.PROTECT, verbose_name='مدرس')

    class Meta:
        verbose_name = 'مدرس های رشته'
        verbose_name_plural = 'مدرس های رشته‌ها'
        unique_together = [['major', 'instructor']]

    def __str__(self) -> str:
        return f'{self.instructor}-{self.major}'


class Instructor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    national_id = models.CharField(
        max_length=10, unique=True,  verbose_name='کدملی')
    majors = models.ManyToManyField(
        Major, through=MajorInstructor, verbose_name='رشته')
    courses = models.ManyToManyField(
        'Course', through='InstructorCourse', verbose_name='درس')

    class Meta:
        verbose_name = 'مدرس'
        verbose_name_plural = 'مدرس‌ها'

    def __str__(self) -> str:
        return f'{self.user.first_name}-{self.user.last_name}'

    def get_majors(self):
        return '، '.join([f'{major.name} ({major.area_of_interest})' for major in self.majors.all()])

    get_majors.short_description = 'رشته‌ها'

    def get_courses(self):
        return '، '.join([course.name for course in self.courses.all()])

    get_courses.short_description = 'درس‌ها'

    @admin.display(ordering='user__first_name')
    def get_first_name(self):
        return self.user.first_name
    get_first_name.short_description = 'نام'

    @admin.display(ordering='user__last_name')
    def get_last_name(self):
        return self.user.last_name
    get_last_name.short_description = 'نام‌خانوادگی'


class InstructorCourse(models.Model):
    course = models.ForeignKey(
        'Course', on_delete=models.PROTECT, verbose_name='درس')
    instructor = models.ForeignKey(
        'Instructor', on_delete=models.PROTECT, verbose_name='مدرس')

    class Meta:
        verbose_name = 'درس ارائه شده'
        verbose_name_plural = 'درس های ارائه شده'
        unique_together = [['course', 'instructor']]

    def __str__(self) -> str:
        return f'{self.instructor}-{self.course}'


class Course(models.Model):
    name = models.CharField(max_length=30, verbose_name='نام')
    code = models.CharField(max_length=10, unique=True, verbose_name='کد درس')
    credit = models.PositiveSmallIntegerField(verbose_name='تعداد واحد')
    semestres = models.ManyToManyField('Semester')

    major = models.ManyToManyField(
        'Major', through='MajorCourse', verbose_name='رشته')

    prerequisite = models.ManyToManyField(
        'self', blank=True, verbose_name='دروس پیشنیاز', symmetrical=False)

    class Meta:
        verbose_name = 'درس'
        verbose_name_plural = 'درس‌ها'

    def __str__(self) -> str:
        return f'{self.name}-{self.credit}'

    def get_majors(self):
        return '، '.join([major.name for major in self.major.all()])
    get_majors.short_description = 'رشته‌ها'

    def get_prerequisite(self):
        return '، '.join([course.name for course in self.prerequisite.all()])
    get_prerequisite.short_description = 'دروس پیشنیاز'


class MajorCourse(models.Model):
    major = models.ForeignKey(
        Major, on_delete=models.PROTECT, verbose_name='رشته')
    course = models.ForeignKey(
        'Course', on_delete=models.PROTECT, verbose_name='درس')

    class Meta:
        verbose_name = 'درس های رشته'
        verbose_name_plural = 'درس های رشته‌ها'
        unique_together = [['major', 'course']]

    def __str__(self) -> str:
        return f'{self.major}-{self.course}'


class Section(models.Model):
    class_time = models.CharField(max_length=100, verbose_name='زمان')
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name='درس')
    instructor = models.ForeignKey(
        Instructor, on_delete=models.CASCADE, verbose_name='مدرس')
    student = models.ManyToManyField(
        Student, through='CourseSelection', verbose_name='دانشجویان')

    class Meta:
        verbose_name = 'سکشن'
        verbose_name_plural = 'سکشن‌ها'

    def __str__(self) -> str:
        return f'{self.course}-{self.instructor}-{self.class_time}'

    def get_students(self):
        return '، '.join([student.id for student in self.student.all()])
    get_students.short_description = 'دانشجویان'


class CourseSelection(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name='دانشجو')
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, verbose_name='سکشن')

    class Meta:
        verbose_name = 'انتخاب واحد'
        verbose_name_plural = 'انتخاب واحد'
        unique_together = [['student', 'section']]

    def __str__(self):
        return f'{self.student}-{self.section}'


class Semester(models.Model):

    FALL = '1'
    WINTER = '2'
    SUMMER = '3'

    SEMESTER_CHOISES = [
        (FALL, 'مهر'),
        (WINTER, 'بهمن'),
        (SUMMER, 'تابستان'),
    ]

    academic_year = models.CharField(max_length=4, verbose_name='سال تحصیلی')
    semester = models.CharField(
        max_length=1, choices=SEMESTER_CHOISES, verbose_name='نیم‌سال ')

    class Meta:
        verbose_name = 'نیم‌سال تحصیلی'
        verbose_name_plural = 'نیم‌سال های تحصیلی'
