from django.db import models

# Create your models here.


class Level(models.Model):
    title = models.CharField(max_length = 3000 , blank = True, default = '')
    is_menu = models.BooleanField(default=False, blank = True, null = True)
    parent_level = models.ForeignKey("Level", blank = True, null = True, on_delete = models.CASCADE )

    def __str__(self):
        return (" Menu: " if self.is_menu else "") + str(self.title)
