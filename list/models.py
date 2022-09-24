from django.db import models

# Create your models here.

class Item(models.Model):
    content = models.TextField()
    completed = models.BooleanField(default=False)

    # class Meta:
    #     ordering = ['-completed']
