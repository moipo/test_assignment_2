from django.db import models

# Create your models here.

class Page(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return str(self.number)


class Level(models.Model):
    title = models.CharField(max_length = 3000 , blank = True, default = '')
    link = models.CharField(max_length = 3000 , blank = True, default = '')
    # has_nested_data = models.BooleanField(default = False, blank = True, null = True)
    is_active = models.BooleanField(default = False, blank = True, null = True)
    is_menu = models.BooleanField(default=False, blank = True, null = True)
    page = models.ForeignKey("Page", blank = True, null = True, on_delete = models.CASCADE )
    parent_level = models.ForeignKey("Level", blank = True, null = True, on_delete = models.CASCADE )

    def __str__(self):
        return (" Menu: " if self.is_menu else "") + str(self.title)
