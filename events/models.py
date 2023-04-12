from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=30)
    subname=models.CharField(max_length=50)
    image = models.ImageField()
    description = models.TextField(max_length=2000)
    venue = models.TextField(max_length=200, default="MMM")
    startDateTime = models.DateTimeField()
    endDateTime = models.DateTimeField()

    def __str__(self) -> str:
        return self.name