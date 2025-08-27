from django.shortcuts import render, get_object_or_404
from .models import Student

def home(request):
    return render(request, "students/home.html")

def student_detail(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    grades = student.grade_set.all()
    return render(request, "students/detail.html", {"student": student, "grades": grades})
