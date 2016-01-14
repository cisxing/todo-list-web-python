from __future__ import unicode_literals

from django.db import models

#run in order, so you have to put List in front of Item
class List(models.Model):
    name = models.TextField(default = '')

class Item(models.Model):
    text = models.TextField(default = '')
    #looking for the wrong key word
    list = models.ForeignKey(List, default=None)
    is_done = models.BooleanField(default = False)
