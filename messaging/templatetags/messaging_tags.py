from django import template
from django.utils.safestring import mark_safe
from messaging.models import Message, Chat
from django.db.models import Count, Case, When


register = template.Library()

@register.simple_tag
def new_messages_number(user):
    pass
    # query_set.aggregate(bool_col=Count(Case(When(my_bool_col=True, then=1))))
    # chats = Chat.objects.all()
    # num = 0
    # for i in chats:
    #     num += i.messages.all().aggregate(is_read=Count(Case(When(is_read=True, then=1))))
