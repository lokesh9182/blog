from django.db import models

# Create your models here.

class tasks(models.Model):
    taskname=models.CharField(max_length=30)
    taskdesc=models.TextField()
    # slug=models.CharField(max_length=30)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.taskname

class task2(models.Model):
    taskname=models.CharField(max_length=30)
    taskdesc=models.TextField()
    slug=models.CharField(max_length=30)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.taskname
