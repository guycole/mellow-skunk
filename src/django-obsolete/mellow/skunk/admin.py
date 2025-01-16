from django.contrib import admin

from .models import Heeler, Hyena, Host, Task

admin.site.register(Heeler)
admin.site.register(Host)
admin.site.register(Hyena)
admin.site.register(Task)