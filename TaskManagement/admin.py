from django.contrib import admin
from .models import User
from .models import Project
from .models import Task
from .models import JustPlan
from .models import Detail
# Register your models here.


class BigAdmin(admin.ModelAdmin):
    fieldsets = [

    ]

admin.site.register(User, BigAdmin)
admin.site.register(Project, BigAdmin)
admin.site.register(Task, BigAdmin)
admin.site.register(JustPlan, BigAdmin)
admin.site.register(Detail, BigAdmin)
