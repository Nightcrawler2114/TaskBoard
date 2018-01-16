from django.db import models
from django.contrib.auth import get_user_model, get_user


class Task(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=1000)
    date = models.DateField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
