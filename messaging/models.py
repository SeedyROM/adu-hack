from django.db import models
from django.utils import timezone
from core.models import UUIDModel
from django.contrib.auth import get_user_model


class Chat(UUIDModel):
    members = models.ManyToManyField(get_user_model())
    timestamp = models.DateTimeField(default=timezone.now)

    @property
    def is_read(self):
        return self.messages.all().filter(is_read=False).exists()

    class Meta:
        ordering = ['timestamp']


class Message(UUIDModel):
    chat = models.ForeignKey(
        Chat, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return self.message
