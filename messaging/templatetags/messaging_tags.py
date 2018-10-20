from django import template
from django.utils.safestring import mark_safe
from messaging.models import Message, Chat
from django.db.models import Count, Case, When


register = template.Library()


@register.simple_tag
def new_messages_number(user):
    chats = Chat.objects.filter(members__in=[user.id])
    num = 0
    for i in chats:
        num += i.messages.all().aggregate(is_read=Count(Case(When(is_read=False, then=1))))['is_read']
    return num
