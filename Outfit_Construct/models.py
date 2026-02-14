from django.db import models
from django.db.models import CASCADE


# Create your models here.
class Drawers(models.Model):
    drawer_id = models.TextField(blank=True, primary_key=True)  # This field type is a guess.
    max_capacity = models.TextField(blank=True, null=True)  # This field type is a guess.
    drawer_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    drawer_description = models.TextField(blank=True, null=True)  # This field type is a guess.
    deleted_at = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'drawers'

class Colours(models.Model):
    colour = models.TextField(blank=True, primary_key=True)  # This field type is a guess.
    complement = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'colours'

class Hexcodes(models.Model):
    hexcode = models.TextField(blank=True, primary_key=True)  # This field type is a guess.
    colour = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'hexcodes'

class Palette(models.Model):
    palette_id = models.TextField(blank=True, primary_key=True)  # This field type is a guess.
    palette_description = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'palette'

class PaletteList(models.Model):
    palette_id = models.TextField(blank=True, null=True) # This field type is a guess.
    colour = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'palette_list'

class Layers(models.Model):
    layer_id = models.TextField(blank=True, primary_key=True)  # This field type is a guess.
    layer_description = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'layers'

class Clothes(models.Model):
    cloth_id = models.TextField(blank=True, primary_key=True)  # This field type is a guess.
    drawer_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    layer_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    colour = models.TextField(blank=True, null=True)  # This field type is a guess.
    hexcode = models.TextField(blank=True, null=True)  # This field type is a guess.
    item_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    cloth_description = models.TextField(blank=True, null=True)  # This field type is a guess.
    deleted_at = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'clothes'

class ClothDetails(models.Model):
    cloth_id = models.TextField(blank=True, primary_key=True)  # This field type is a guess.
    image = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'cloth_details'

"""
# old models

class Drawers(models.Model):
    drawer_id = models.AutoField(primary_key=True)
    max_capacity = models.IntegerField(blank=False, null=False)
    drawer_type = models.TextField(blank=False, null=False, max_length=6)
    drawer_description = models.TextField(blank=True, null=True, max_length=50)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drawers'

class Colours(models.Model):
    colour = models.TextField(primary_key=True, max_length=20)
    complement = models.TextField(blank=True, null=True, max_length=20)
    class Meta:
        managed = False
        db_table = 'colours'

class Hexcodes(models.Model):
    hexcode = models.TextField(primary_key=True, max_length=7)
    colour = models.ForeignKey(Colours, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'hexcodes'

class Palette(models.Model):
    palette_id = models.AutoField(primary_key=True)
    palette_description = models.TextField(blank=True, null=True, max_length=50)
    class Meta:
        managed = False
        db_table = 'palette'

class PaletteList(models.Model):
    palette_id = models.ForeignKey(Palette, on_delete=models.CASCADE)
    colour = models.ForeignKey(Colours, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'palette_list'

class Layers(models.Model):
    layer_id = models.AutoField(primary_key=True)
    layer_description = models.TextField(blank=True, null=True, max_length=50)
    class Meta:
        managed = False
        db_table = 'layers'

class Clothes(models.Model):
    cloth_id = models.AutoField(primary_key=True)
    drawer_id = models.ForeignKey(Drawers, on_delete=models.CASCADE)
    layer_id = models.ForeignKey(Layers, on_delete=models.CASCADE)
    colour = models.ForeignKey(Colours, on_delete=models.CASCADE)
    hexcode = models.ForeignKey(Hexcodes, on_delete=models.CASCADE)
    item_type = models.TextField(blank=True, null=True, max_length=6)
    cloth_description = models.TextField(blank=True, null=True, max_length=50)
    deleted_at = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'clothes'

class ClothDetails(models.Model):
    cloth_id = models.ForeignKey(Clothes, on_delete=models.CASCADE)
    image = models.TextField(blank=True, null=True, max_length=260)

"""
