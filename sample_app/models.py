from django.db import models
from datetime import datetime

# Create your models here.
class CMS(models.Model):
    heading = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.heading