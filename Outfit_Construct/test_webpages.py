from django.test import TestCase,SimpleTestCase
from Outfit_Construct.models import Drawers, Clothes, Colours, Hexcodes, Palette, PaletteList, Layers
from django import forms
from Outfit_Construct.views import outfit_suggest
from django.urls import reverse
from django.shortcuts import render

class TutorialTest(TestCase):
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
        Clothes.objects.create(cloth_id='4', drawer_id_id="1", layer_id_id="1", colour_id="Black", hexcode_id="#000000",
                               item_type="bottom", cloth_description="TestCase Cloth Creation bottom")
        Palette.objects.create(palette_id="2", palette_description="Reds")
        Palette.objects.create(palette_id="3", palette_description="Blues")


    def test_createPage_response(self):
        response = self.client.get(reverse('createPage'))
        self.assertEqual(response.status_code, 200) #This checks if the webpage is responsive

    def test_createPage(self):
        response = self.client.get(reverse('createPage'))
        self.assertEqual(response.context['count'], 0) #This helps to check if context values are entered correctly
        self.assertTemplateUsed(response, 'create.html') #This checks if the correct template is being used

    def test_homePage_response(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homePage(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'index.html')



    #Modify these tests

    def test_editPage_response(self):
        response = self.client.get(reverse('edit_clothing'))
        self.assertEqual(response.status_code, 200)

    def test_editPage(self):
        response = self.client.get(reverse('edit_clothing'))
        self.assertTemplateUsed(response, 'edit_clothing.html')

    def test_createClothing_response(self):
        response = self.client.get(reverse('create_clothing'))
        self.assertEqual(response.status_code, 200)

    def test_createClothing(self):
        response = self.client.get(reverse('create_clothing'))
        self.assertTemplateUsed(response, 'create_clothing.html')

    def test_selectedPalette_response(self):
        response = self.client.get(reverse('selected_palette'))
        self.assertEqual(response.status_code, 200)

    def test_selectedPalette(self):
        response = self.client.get(reverse('selected_palette'))
        self.assertTemplateUsed(response, 'selected_colour.html')

    def test_selectedClothing(self):
        response = self.client.get(reverse('selected_clothing'))
        self.assertTemplateUsed(response, 'selected_clothing.html')

    def test_clothingHome_response(self):
        response = self.client.get(reverse('clothing_home'))
        self.assertEqual(response.status_code, 200)

    def test_clothingHome(self):
        response = self.client.get(reverse('clothing_home'))
        self.assertTemplateUsed(response, 'clothing_home.html')

    def test_selectedDrawer_response(self):
        response = self.client.get(reverse('selected_drawer'))
        self.assertEqual(response.status_code, 200)

    def test_selectedDrawer(self):
        response = self.client.get(reverse('selected_drawer'))
        self.assertTemplateUsed(response, 'selected_drawer.html')

"""
# old tests
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
        response = self.client.get('/Outfit_Construct/clothing/')
        self.assertEqual(response.status_code, 200)

    def test_createPage(self):
        response = self.client.get('/Outfit_Construct/closet/')
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
"""