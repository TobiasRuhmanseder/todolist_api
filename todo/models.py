import datetime
from pydoc import describe
from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title= models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    created_at = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def time_passed(self):
        today = datetime.date.today()
        delta = today - self.created_at
        return delta.days
