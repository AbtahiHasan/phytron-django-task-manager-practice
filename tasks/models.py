from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField()
    start_date = models.DateField()


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    employee = models.ManyToManyField(Employee)
    title = models.CharField(max_length=250)
    description = models.TextField()
    due_date = models.DateField()
    is_completed = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TaskDetails(models.Model):
    HIGH = "H"
    MEDEUM = "M"
    LOW = "L"
    PRIORITY_OPTIONS = ((HIGH, "HIGH"), (MEDEUM, "MEDEUM"), (LOW, "LOW"))
    task = models.OneToOneField(
        Task,
        on_delete=models.CASCADE,
    )
    assign_to = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=PRIORITY_OPTIONS, default=LOW)
