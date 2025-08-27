'''from django.contrib import admin
from .models import Student, Course, Grade

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Grade)'''

from django.contrib import admin
from .models import Student, Course, Grade

# Customize how Student appears
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "name", "department", "level", "gpa")  # columns shown
    search_fields = ("student_id", "name", "department")  # search box
    list_filter = ("department", "level")  # filters on right side

class CourseAdmin(admin.ModelAdmin):
    list_display = ("code", "title", "credit")
    search_fields = ("code", "title")

class GradeAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "score", "grade")
    search_fields = ("student__name", "course__code")
    list_filter = ("grade",)

# Register models
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Grade, GradeAdmin)
