from django import template

register = template.Library()

@register.filter
def reemplazar_coma(value):
    return value.replace(",", ".")