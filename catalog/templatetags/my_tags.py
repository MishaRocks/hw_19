from django import template

register = template.Library()


@register.filter
def mymedia(val):
    if val:
        return f'/media/{val}'
    return "/media/products/img.png"


@register.simple_tag
def mediapath(val):
    if val:
        return f'/media/{val}'
    return "/media/products/img.png"


@register.filter
def rub(val):
    return f'{val} руб.'
