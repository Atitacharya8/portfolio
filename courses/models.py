from django.db import models

# Create your models here.

class Course(models.Model):
    image=models.ImageField(upload_to='media/')
    summary=models.CharField(max_length=250)

    def __str__(self):
        return self.summary
