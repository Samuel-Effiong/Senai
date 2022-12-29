
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter('separate_tools')
@stringfilter
def separate_tools(value: str):
    return value.split(',')
