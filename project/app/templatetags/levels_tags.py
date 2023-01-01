from django import template
from app.models import *

register = template.Library()



@register.inclusion_tag('inclusion_tags/draw_menu.html', takes_context = True)
def draw_menu(context, title = None):
    unfolded_items = context.get('unfolded_items')
    menues = Level.objects.filter(title = title)
    return {"menues" : menues, "unfolded_items":unfolded_items}
