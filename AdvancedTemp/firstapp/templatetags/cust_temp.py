from django import template
register=template.Library()


@register.filter(name='f3upper')
def upperthree(value):
    result=value[:3].upper()
    return result
    