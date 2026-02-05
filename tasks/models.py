from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    start_at = models.DateField()

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=1)
    assign_to = models.ManyToManyField(Employee, related_name="employees")


class TaskDetails(models.Model):
    PRIORITY_OPTIONS = (
        ('H', 'HIGH'),
        ('M', 'MEDIUM'),
        ('L', 'LOW')
    )
    assign_to = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=PRIORITY_OPTIONS, default='L')
