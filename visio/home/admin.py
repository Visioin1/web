from django.contrib import admin

# Register your models here.
from .models import Home,Internships,jobs

admin.site.register(Home)
admin.site.register(Internships)
admin.site.register(jobs)