
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter('separate_tools')
@stringfilter
def separate_tools(value: str):
    return value.split(',')


# @register.inclusion_tag(filename='portfolio_display.html', takes_context=True, name='display_tag')

@register.filter('ravel_zip')
def ravel_zip(iterator):
    ravel = [i for items in iterator for i in items if i is not None]

    return ravel
