from __future__ import unicode_literals

from django.db import models

#run in order, so you have to put List in front of Item
class List(models.Model):
    pass

class Item(models.Model):
    text = models.TextField(default = '')
    #looking for the wrong key word
    list = models.ForeignKey(List, default=None)
