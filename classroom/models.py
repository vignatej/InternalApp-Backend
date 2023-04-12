from django.db import models
from users.models import profile
# Create your models here.
class ClassRoom(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    year = models.IntegerField()
    semChoices = [('even',"even"),("odd", "odd")]
    sem = models.CharField(choices = semChoices, max_length=5)
    teacher_name = models.CharField(max_length=50)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(profile, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return F"{self.name}-{self.code}"


class Posts(models.Model):
    classRoom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    description = models.TextField()
    created_by = models.ForeignKey(profile, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

class BucketItems(models.Model):
    file = models.FileField(upload_to="files/")
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    created_by = models.ForeignKey(profile, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

