from django.db import models

# Create your models here.
from django.db import models

class SampleData(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user_email = models.EmailField()

    def __str__(self):
        return self.title
