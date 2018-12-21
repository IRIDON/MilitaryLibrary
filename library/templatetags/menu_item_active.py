from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def menu_item_active(context, value):
    try:
        view_name = context['request'].resolver_match.view_name
    except:
        return ''

    if view_name == value:
        return '__active'
