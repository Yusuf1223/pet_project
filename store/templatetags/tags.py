from django import template

register = template.Library()


@register.filter
def cart(things, status):
    return len(things.filter(status=status))

