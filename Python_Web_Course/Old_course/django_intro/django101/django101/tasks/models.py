from django.db import models

class Task(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
    )
    description = models.TextField()
    priority = models.IntegerField(default=0)
