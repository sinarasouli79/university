from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from main.models import Course
# Create your views here.
@login_required
def home(request, *args, **kwargs):
    return render(request, 'home.html', {})


class Home(LoginRequiredMixin, ListView):
    queryset = Course.objects.all()
    template_name = 'home.html'