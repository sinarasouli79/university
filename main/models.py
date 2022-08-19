from django.db import models

# Create your models here.


class Faculty(models.Model):
    name = models.CharField(max_length=30)
    manager = models.CharField(max_length=30)
    established_year = models.DateField()

    def __str__(self) -> str:
        return self.name


class Major(models.Model):
    BACHELOR = 'B'
    MASTER = 'M'
    DOCTORATE = 'D'
    GRADE_CHOISES = [
        (BACHELOR, 'BACHELOR'),
        (MASTER, 'MASTER'),
        (DOCTORATE, 'DOCTORATE'),
    ]
    name = models.CharField(max_length=100)
    grade = models.CharField(
        max_length=1, choices=GRADE_CHOISES, default=BACHELOR)
    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f'{self.name}'


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    major = models.ForeignKey(Major, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f'{self.first_name}-{self.last_name}'


class MajorInstructor(models.Model):
    major = models.ForeignKey(Major, on_delete=models.PROTECT)
    instructor = models.ForeignKey('Instructor', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f'{self.instructor}-{self.major}'


class Instructor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    major = models.ManyToManyField(Major, through=MajorInstructor)
    course = models.ManyToManyField('Course', through='InstructorCourse')

    def __str__(self) -> str:
        return f'{self.first_name}-{self.last_name}'


class InstructorCourse(models.Model):
    course = models.ForeignKey('Course', on_delete=models.PROTECT)
    instructor = models.ForeignKey('Instructor', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f'{self.instructor}-{self.course}'


class Course(models.Model):
    name = models.CharField(max_length=30)
    credit = models.SmallIntegerField()
    major = models.ManyToManyField('Major', through='MajorCourse')

    prerequisite = models.ManyToManyField(
        'self', blank=True)

    def __str__(self) -> str:
        return f'{self.name}-{self.credit}'


class MajorCourse(models.Model):
    major = models.ForeignKey(Major, on_delete=models.PROTECT)
    course = models.ForeignKey('Course', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f'{self.major}-{self.course}'


class Section(models.Model):
    class_time = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student, through='CourseSelection')

    def __str__(self) -> str:
        return f'{self.course}-{self.instructor}-{self.class_time}'


class CourseSelection(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student}-{self.section}'