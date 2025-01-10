from django.contrib import admin

from .models import Heeler, Host, Task

admin.site.register(Heeler)
admin.site.register(Host)
admin.site.register(Task)