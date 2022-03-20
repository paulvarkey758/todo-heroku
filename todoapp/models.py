from django.db import models

# Create your models here.
class Todolist(models.Model):
    task=models.TextField(max_length=50)

    def __str__(self):
        return self.task[0:10]