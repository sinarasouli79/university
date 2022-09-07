from django import forms


class CourseSelectionForm(forms.Form):
    course_code = forms.CharField()
    section_code = forms.CharField()
