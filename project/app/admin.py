from django.contrib import admin
from .models import *

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    exclude = tuple()
    class Meta:
        model = Page
admin.site.register(Page, PageAdmin)

class LevelAdmin(admin.ModelAdmin):
    exclude = tuple()
    class Meta:
        model = Level
admin.site.register(Level, LevelAdmin)
