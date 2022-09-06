from django import forms


class StudentCourseSelection(forms.Form):
    course_code = forms.CharField()
    section_code = forms.CharField()
