from django import template

register = template.Library()

@register.simple_tag
def mediapath(path):
    return f"/media/{path}"

@register.filter
def mediapath(path):
    return f"/media/{path}"