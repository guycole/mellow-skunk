from django.contrib import admin

from .models import Host, Task

admin.site.register(Host)
admin.site.register(Task)
