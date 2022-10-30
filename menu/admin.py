from django.contrib import admin
from menu.models import *

myModels = [Sections, Items, Modifiers]  # iterable list
admin.site.register(myModels)
