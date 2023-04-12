from django.db import models
from users.models import profile
# Create your models here.

class Message(models.Model):
    sender = models.ForeignKey(profile, on_delete=models.CASCADE, related_name="senders")
    reciever = models.ForeignKey(profile, on_delete=models.CASCADE, related_name="recievers")
    text = models.TextField(max_length=10000)
    room = models.CharField(max_length=20, null=False)
    created_time = models.DateTimeField(auto_now_add=True)