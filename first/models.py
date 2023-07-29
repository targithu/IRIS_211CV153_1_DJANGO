from random import choice
from django.db import models
import datetime
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    club = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(validators=[MinValueValidator(datetime.date.today)], null=True)
    
    MEDIA_CHOICES = (
        ("Instagram", "Instagram"),
        ("Whatsapp", "Whatsapp"),
        ("LinkedIn", "LinkedIn"),
    )
    socialmedia = models.CharField(max_length=9, choices=MEDIA_CHOICES, default="LinkedIn")

    def __str__(self):
        return f"{self.title} {self.description} {self.deadline} {self.socialmedia}"


class SubTasks(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE,related_name='subtasks')
    sub_title = models.CharField(max_length=200)
    sub_description = models.TextField()
    sub_deadline = models.DateField(validators=[MinValueValidator(datetime.date.today)], null=True)

    def __str__(self):
        return f"{self.task} {self.sub_title} {self.sub_description} {self.sub_deadline} "

    


