from django.db import models
from users.models import profile
# Create your models here.
class story(models.Model):
    user= models.ForeignKey(profile, null=True, on_delete=models.CASCADE)
    Text = models.TextField(max_length=5000)

class question(models.Model):
    user= models.ForeignKey(profile, null=True, on_delete=models.CASCADE)
    story=models.ForeignKey(story,null=False,on_delete=models.CASCADE)
    Text= models.TextField(max_length=200)

class answer(models.Model):
    user= models.ForeignKey(profile, null=True, on_delete=models.CASCADE)
    question = models.ForeignKey(question, null=False, on_delete=models.CASCADE) 
    Text = models.TextField(max_length=2000)
