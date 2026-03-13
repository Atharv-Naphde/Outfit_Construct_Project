from django.db import models
from django.db.models import CASCADE


# Create your models here.
class Drawers(models.Model):
    drawer_id = models.TextField(blank=True, primary_key=True)  # This field type is a guess.
    max_capacity = models.IntegerField(blank=True, null=True)  # This field type is a guess.
    drawer_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    drawer_description = models.TextField(blank=True, null=True, max_length=50)  # This field type is a guess.
    deleted_at = models.DateField  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'drawers'
        verbose_name_plural = "Drawers"

class Colours(models.Model):
    colour = models.TextField(blank=True, primary_key=True, max_length=20)  # This field type is a guess.
    complement = models.TextField(blank=True, null=True, max_length=20)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'colours'
        verbose_name_plural = "Colours"

class Hexcodes(models.Model):
    hexcode = models.TextField(blank=True, primary_key=True, max_length=7)  # This field type is a guess.
    colour = models.ForeignKey("Colours", on_delete=models.CASCADE, db_column='colour')

    class Meta:
        managed = True
        db_table = 'hexcodes'
        verbose_name_plural = "Hexcodes"

class Palette(models.Model):
    palette_id = models.IntegerField(blank=True, primary_key=True)  # This field type is a guess.
    palette_description = models.TextField(blank=True, null=True, max_length=50)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'palette'
        verbose_name_plural = "Palette"

class PaletteList(models.Model):
    palette_list_id = models.IntegerField(blank=True, primary_key=True)
    # use makemigrations to fix any errors.
    palette_id = models.ForeignKey(Palette, on_delete=models.CASCADE, db_column='palette_id')
    colour = models.ForeignKey(Colours, on_delete=models.CASCADE, db_column='colour')

    class Meta:
        managed = True
        db_table = 'palette_list'
        verbose_name_plural = "PaletteList"

class Layers(models.Model):
    layer_id = models.TextField(blank=True, primary_key=True)  # This field type is a guess.
    layer_description = models.TextField(blank=True, null=True, max_length=50)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'layers'
        verbose_name_plural = "Layers"

class Clothes(models.Model):
    cloth_id = models.TextField(blank=True, primary_key=True)
    drawer_id = models.ForeignKey(Drawers, on_delete=models.CASCADE, db_column='drawer_id')
    layer_id = models.ForeignKey(Layers, on_delete=models.CASCADE, db_column='layer_id')
    colour = models.ForeignKey(Colours, on_delete=models.CASCADE, db_column='colour')
    hexcode = models.ForeignKey(Hexcodes, on_delete=models.CASCADE, db_column='hexcode')
    item_type = models.TextField(blank=True, null=True, max_length=6)
    cloth_description = models.TextField(blank=True, null=True, max_length=50)
    deleted_at = models.DateField
    #image = models.ImageField(blank=True, null=True, upload_to="images/")
    class Meta:
        managed = True
        db_table = 'clothes'
        verbose_name_plural = "Clothes"


class ClothDetails(models.Model):
    # The column below does not exist in the database or test data, and is used only to enure proper functioning of the django model.
    cloth_details_id = models.IntegerField(blank=True, primary_key=True)
    # use makemigrations to fix any errors.
    cloth_id = models.ForeignKey("Clothes", on_delete=models.CASCADE, db_column='cloth_id')
    # image = models.TextField(blank=True, null=True)  # This field type is a guess.
    image = models.ImageField(blank=True, null=True, upload_to="images/")

    class Meta:
        managed = True
        db_table = 'cloth_details'
        verbose_name_plural = "ClothDetails"
