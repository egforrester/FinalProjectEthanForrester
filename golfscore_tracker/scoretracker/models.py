from django.db import models
from django.contrib.auth.models import User

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    course_name = models.CharField(max_length=100)
    scores = models.JSONField()  # Stores scores for each hole

    def __str__(self):
        return f"{self.user.username} on {self.date} at {self.course_name}"
