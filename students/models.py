from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    level = models.CharField(max_length=20)  # e.g. "100", "200"
    gpa = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class Course(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    credit = models.IntegerField()

    def __str__(self):
        return self.title

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.FloatField()
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.student.name} - {self.course.code}"
