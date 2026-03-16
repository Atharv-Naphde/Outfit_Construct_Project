from django.test import TestCase,SimpleTestCase
from Outfit_Construct.models import Drawers, Clothes, Colours, Hexcodes, Palette, PaletteList, Layers
from django import forms
from Outfit_Construct.views import outfit_suggest
from django.shortcuts import render
"""
To run tests, use the following commands:

python manage.py test
 
"""

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
        Clothes.objects.create(cloth_id='2',drawer_id_id="1",layer_id_id="1",colour_id="White",hexcode_id="#FFFFFF",item_type="bottom",cloth_description="TestCase Cloth Creation Bottom")


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
            self.fail("(Intentional Fail) Invalid cloth id, No outfit suggestions.")

# The template tests will not work without a proper setup class
# follow the tutorial at https://www.youtube.com/watch?v=GOxdQLrEX5U to make these better.
class TestTemplates(TestCase):

    def setUp(self):
        # Setup the database
        Drawers.objects.create(drawer_id="1", max_capacity="30", drawer_type="top",
                               drawer_description="TestCase Drawer Creation")
        Layers.objects.create(layer_id="1", layer_description="TestCase Layer Creation")
        Colours.objects.create(colour="Black", complement="White")
        Colours.objects.create(colour="White", complement="Black")
        Hexcodes.objects.create(hexcode="#FFFFFF", colour_id="White")
        Hexcodes.objects.create(hexcode="#000000", colour_id="Black")
        Palette.objects.create(palette_id="1", palette_description="Greyscale")
        PaletteList.objects.create(palette_list_id="1", palette_id_id="1", colour_id="Black")
        PaletteList.objects.create(palette_list_id="2", palette_id_id="1", colour_id="White")
        Clothes.objects.create(cloth_id='1', drawer_id_id="1", layer_id_id="1", colour_id="Black", hexcode_id="#000000",
                               item_type="top", cloth_description="TestCase Cloth Creation Top")

        # The values below are genarated to help test the other functions
        Clothes.objects.create(cloth_id='3', drawer_id_id="1", layer_id_id="1", colour_id="White", hexcode_id="#FFFFFF",
                               item_type="bottom", cloth_description="TestCase Creation for deletion")

    def test_homePage_response(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)



    def test_homePage(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_createPage_response(self):
        response = self.client.get('/closet/')
        self.assertEqual(response.status_code, 200)

    def test_createPage(self):
        response = self.client.get('/closet/')
        self.assertTemplateUsed(response, 'create.html')

    def test_editPage_response(self):
        response = self.client.get('/clothing/edit/')
        self.assertEqual(response.status_code, 200)

    def test_editPage(self):
        response = self.client.get('/clothing/edit/')
        self.assertTemplateUsed(response, 'edit_clothing.html')

    def test_deletePage_response(self):
        response = self.client.get('/clothing/delete/')
        self.assertEqual(response.status_code, 200)

    def test_deletePage(self):
        response = self.client.get('/clothing/delete/')
        self.assertTemplateUsed(response, 'delete.html')

    def test_createClothing_response(self):
        response = self.client.get('/clothing/create/')
        self.assertEqual(response.status_code, 200)

    def test_createClothing(self):
        response = self.client.get('/clothing/create/')
        self.assertTemplateUsed(response, 'create_clothing.html')

    def test_selectedPalette_response(self):
        response = self.client.get('/palette/')
        self.assertEqual(response.status_code, 200)

    def test_selectedPalette(self):
        response = self.client.get('/palette/')
        self.assertTemplateUsed(response, 'selected_colour.html')

    def test_selectedClothing(self):
        response = self.client.get('/clothing/select/')
        self.assertTemplateUsed(response, 'selected_clothing.html')


    def test_clothingHome_response(self):
        response = self.client.get('/clothing/home')
        self.assertEqual(response.status_code, 200)

    def test_clothingHome(self):
        response = self.client.get('/clothing/home/')
        self.assertTemplateUsed(response, 'clothing_home.html')


    def test_selectedDrawer_response(self):
        response = self.client.get('/drawer/')
        self.assertEqual(response.status_code, 200)

    def test_selectedDrawer(self):
        response = self.client.get('/drawer/')
        self.assertTemplateUsed(response, 'selected_drawer.html')