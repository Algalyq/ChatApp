from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    UserId = models.ForeignKey(User, on_delete=models.CASCADE,related_name="sendUser")
    ToUser = models.ForeignKey(User, on_delete=models.CASCADE,related_name="toUser")
    Timest = models.TimeField()
    Msg = models.TextField(max_length=1000)