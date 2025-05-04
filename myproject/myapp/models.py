from django.db import models
from django.contrib.auth.models import User
import uuid

class University(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    website = models.URLField()

    def __str__(self):
        return self.name

class Faculty(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    required_score = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.university.name}"

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interests = models.JSONField(default=list)
    saved_faculties = models.ManyToManyField(Faculty, blank=True)

    def __str__(self):
        return self.user.username

class Camp(models.Model):  # เปลี่ยนจาก Review เป็น Camp
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=255)
    website = models.URLField()
    
    def __str__(self):
        return self.title

class News(models.Model):  # เพิ่ม News Model
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


