from django import template

register = template.Library()

@register.filter
def only_active(comments):
    return comments.filter(active= True)
