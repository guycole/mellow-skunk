from django.shortcuts import render

from django.http import HttpResponse

from django.views import generic

from .models import Heeler, Host, Hyena, Task

def index(request):
    host_list = Host.objects.filter(active_flag=True) # should only be one
    task_list = Task.objects.all() # empty to many
    context = {"host_list": host_list, "task_list": task_list}
    return render(request, 'skunk/index.html', context)

class HeelerView(generic.ListView):
    template_name = "skunk/heeler.html"

    context_object_name = "observation_list"

    def get_queryset(self):
        return Heeler.objects.all()

class HyenaView(generic.ListView):
    template_name = "skunk/hyena.html"

    context_object_name = "observation_list"

    def get_queryset(self):
        return Hyena.objects.all()
