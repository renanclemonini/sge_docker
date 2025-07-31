from django import template
from django.utils.formats import number_format

register = template.Library()


@register.filter
def format_currency(value):
    return number_format(value, decimal_pos=2, force_grouping=True)
