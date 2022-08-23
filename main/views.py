from django.shortcuts import render
from .models import (Student)
# Create your views here.


def student_list(request, *arg, **kwargs):
    queryset = Student.objects.all()
    context = {'queryset': queryset}
    return render(request, 'student-detail-list.html', context)
