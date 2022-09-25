from django.db import models

# Create your models here.
class Task(models.Model):
    title =  models.CharField(max_length=255)
    description = models.TextField()
    technology = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)