from django.db import models

# Create your models here.

class Page(models.Model):
    number = models.IntegerField()


class Level(models.Model):
    title = models.CharField(max_length = 3000 , blank = True, default = '')
    link = models.CharField(max_length = 3000 , blank = True, default = '')
    has_nested_data = models.BooleanField(default = False, blank = True, null = True)
    is_active = models.BooleanField(default = False, blank = True, null = True)
    is_menu = models.BooleanField(default=False, blank = True, null = True)
    page = models.ForeignKey("Page", blank = True, null = True, on_delete = models.CASCADE )
    parent_level = models.ForeignKey("Level", blank = True, null = True, on_delete = models.CASCADE )
