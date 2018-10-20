from django import template
from django.utils.safestring import mark_safe
from messaging.models import Message, Chat

register = template.Library()

@register.simple_tag
def new_messages_number(user):
    chats = Chat.objects.filter(members__in=[user.id])