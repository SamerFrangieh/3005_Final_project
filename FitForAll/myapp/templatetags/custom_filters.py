from django import template

register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter(name='format_hour')
def format_hour(hour):
    return "{:02}:00".format(hour)
