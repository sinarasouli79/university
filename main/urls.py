from django.urls import path
from .views import student_list
app_name = 'main'

urlpatterns = [
    path('', student_list, name='student-list')
]
