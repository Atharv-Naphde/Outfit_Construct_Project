from django.test import TestCase,SimpleTestCase
from Outfit_Construct.models import Drawers, Clothes, Colours, Hexcodes, Palette, PaletteList, Layers
from django import forms
from Outfit_Construct.views import outfit_suggest
from django.shortcuts import render
"""
To run tests, use the following commands:

python manage.py test

"""
# End-to-end tests using pyTest
# Create your tests here.

# Django uses a separate database while testing, which does not contain any objects.
class ViewEverythingTest(TestCase):
    def setUp(self):
        # Setup the database
        Drawers.objects.create(drawer_id="1",max_capacity="30",drawer_type="top",drawer_description= "TestCase Drawer Creation")
        Layers.objects.create(layer_id="1",layer_description="TestCase Layer Creation")
        Colours.objects.create(colour="Black",complement="White")
        Colours.objects.create(colour="White", complement="Black")
        Hexcodes.objects.create(hexcode="#FFFFFF", colour_id="White")
        Hexcodes.objects.create(hexcode="#000000",colour_id="Black")
        Palette.objects.create(palette_id="1",palette_description="Greyscale")
        PaletteList.objects.create(palette_list_id="1",palette_id_id="1",colour_id="Black")
        PaletteList.objects.create(palette_list_id="2", palette_id_id="1", colour_id="White")
        Clothes.objects.create(cloth_id='1',drawer_id_id="1",layer_id_id="1",colour_id="Black",hexcode_id="#000000",item_type="top",cloth_description="TestCase Cloth Creation Top")

        # The values below are genarated to help test the other functions
        Clothes.objects.create(cloth_id='3', drawer_id_id="1", layer_id_id="1", colour_id="White", hexcode_id="#FFFFFF",
                               item_type="bottom", cloth_description="TestCase Creation for deletion")

    def test_view_everything(self):
        #The test database does not use the normal database, but creates a new one while testing.
        clothes = Clothes.objects.get(cloth_id = '1')
        drawers = Drawers.objects.get(drawer_id = '1')
        layers = Layers.objects.get(layer_id = '1')
        colours = Colours.objects.get(colour = 'Black')
        hexcodes = Hexcodes.objects.get(hexcode = '#FFFFFF')
        palette = Palette.objects.get(palette_id = '1')
        palette_list = PaletteList.objects.get(palette_list_id = '1')
        # If no errors in console show up, everything is working.

    def test_view_clothes(self):
        clothes = Clothes.objects.all()
        cloth1 = clothes[0].cloth_description

    def test_add_clothes(self):
        Clothes.objects.create(cloth_id='2',drawer_id_id="1",layer_id_id="1",colour_id="White",hexcode_id="#FFFFFF",
                               item_type="bottom",cloth_description="TestCase Cloth Creation Bottom")


    def test_modify_clothes(self):

        cloth1 = Clothes.objects.get(cloth_id='1')
        cloth1.cloth_description = "TestCase Cloth Update Top"
        cloth1.save()
        if (Clothes.objects.get(cloth_id='1').cloth_description == "TestCase Cloth Creation Top"):
            self.fail("Cloth has not been updated")

    def test_delete_clothes(self):
        try:
            Clothes.objects.get(cloth_id='3').delete()
        except:
            self.fail("Cloth has not been deleted")

    def test_outfit_suggestons(self):
        clothes = outfit_suggest("1")
        desc = clothes[0].cloth_description #This will throw an error if there aren't any matching clothes


    # Below this comment are test cases where the choices are invalid. These are intended to fail.

    def test_invalid_outfit_suggestions(self):
        try:
            clothes = outfit_suggest("blabla")
        except:
            print("Invalid Cloth ID")
            #self.fail("(Intentional Fail) Invalid cloth id, No outfit suggestions.")