from django.db import models
from django.utils import timezone
from core.models import UUIDModel


class Chat(UUIDModel, models.Model):
    members = models.ManyToManyField('accounts.User')
    timestamp = models.DateTimeField(default=timezone.now)

    def is_read(self):
        return self.messages.all().filter(is_read=False).exists()

    class Meta:
        ordering = ['timestamp']

class Message(UUIDModel, models.Model):
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return self.message

