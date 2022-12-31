from django import template
from app.models import *

register = template.Library()

# @register.simple_tag(name="get_menu")
# def get_menu(page_filter=None):
#     if filter is not None:
#         menu = Level.objects.filter(page=page_filter)
#     else:
#         menu = Level.objects.filter(page = 1)
#     return menu


@register.inclusion_tag('inclusion_tags/draw_menu.html')
def draw_menu(title = None):
    menues = Level.objects.filter(title = title)
    # menues = Level.objects.filter(page = 1)
    return {"menues" : menues}
