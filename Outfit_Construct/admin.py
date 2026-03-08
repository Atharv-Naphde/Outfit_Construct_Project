from django.contrib import admin

import Outfit_Construct
from Outfit_Construct.models import *
# Register your models here.
admin.site.register(Clothes)
admin.site.register(Drawers)
admin.site.register(Colours)
admin.site.register(Layers)
admin.site.register(Hexcodes)
admin.site.register(ClothDetails)
admin.site.register(PaletteList)
admin.site.register(Palette)