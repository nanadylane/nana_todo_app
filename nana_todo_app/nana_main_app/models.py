from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class NanaTask(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    STATUS = [
        ('Done','Done'),
        ('In Progress','In Progress'),
    ]
    status = models.CharField(max_length=255, choices = STATUS)
    due_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class NanaTag(models.Model):
    tag_name = models.CharField( max_length=255)
    tasks = models.ManyToManyField(NanaTask)
    
