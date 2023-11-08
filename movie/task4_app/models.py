from django.db import models


# Create your models here.
class Task4(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    image = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name
