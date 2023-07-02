from random import choice
from django.db import models
import datetime
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    deadline=models.DateField(validators=[MinValueValidator(datetime.date.today)],null=True)
    MEDIA_CHOICES = (
    ("Instagram", "Instagram"),
    ("Whatsapp", "Whatsapp"),
    ("LinkedIn", "LinkedIn"),
)
    socialmedia=models.CharField(max_length=9,choices=MEDIA_CHOICES,default="LinkedIn")
    def __str__(self):
        return  f"{self.title} {self.description} {self.deadline} {self. socialmedia}"

class SubTasks(Task):
    status=models.BooleanField(default=False)
    deadlin=models.DateField(validators=[MinValueValidator(datetime.date.today)],null=True)
    def __str__(self):
        return f"{self.title} {self.description} {self.deadlin} {self.status}"
    


