from django.http import HttpResponse,Http404
from django.shortcuts import render
from django.template import loader
from Outfit_Construct.models import Drawers, Clothes, Colours, Hexcodes, Palette, PaletteList, Layers


# Create your views here.
def home(request):
    template = loader.get_template('index.html')
    random_clothes = Clothes.objects.all().order_by('?')
    cloth1 = random_clothes[0]
    cloth2 = random_clothes[1]
    cloth3 = random_clothes[2]
    random_palette = Palette.objects.all().order_by('?')
    palette1 = random_palette[0]
    palette2 = random_palette[1]
    palette3 = random_palette[2]
    temp = "Temp Function"
    placeholder_link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    context = {
        'temp' : temp,
        'cloth1_link' : placeholder_link,
        'cloth1_name' : cloth1.cloth_description,
        'cloth2_link' : placeholder_link,
        'cloth2_name' : cloth2.cloth_description,
        'cloth3_link' : placeholder_link,
        'cloth3_name' : cloth3.cloth_description,

        'palette1_link' : placeholder_link,
        'palette1_name' : palette1.palette_description,
        'palette2_link' : placeholder_link,
        'palette2_name' : palette2.palette_description,
        'palette3_link' : placeholder_link,
        'palette3_name' : palette3.palette_description,
    }
    return HttpResponse(template.render(context, request))


def random_drawer(request):
    random_item = Drawers.objects.all().order_by('?').first()
    description = random_item.drawer_description
    template = loader.get_template('index.html')
    context = {'temp' : description}
    return HttpResponse(template.render(context, request))

def random_clothes(request):
    random_item = Clothes.objects.all().order_by('?').first()
    description = random_item.cloth_description
    template = loader.get_template('index.html')
    context = {
        'temp' : description
    }
    return HttpResponse(template.render(context, request))

def random_colour(request):
    random_item = Colours.objects.all().order_by('?').first()
    description = random_item.colour
    template = loader.get_template('index.html')
    context = {'temp' : description}
    return HttpResponse(template.render(context, request))

def random_hexcode(request):
    random_item = Hexcodes.objects.all().order_by('?').first()
    description = random_item.hexcode #colour_id
    template = loader.get_template('index.html')
    context = {'temp' : description}
    return HttpResponse(template.render(context, request))

def random_palette(request):
    random_item = Palette.objects.all().order_by('?').first()
    description = random_item.palette_description
    template = loader.get_template('index.html')
    context = {'temp' : description}
    return HttpResponse(template.render(context, request))

def random_palette_list(request):
    random_item = PaletteList.objects.all().order_by('?').first()
    description = random_item.colour
    template = loader.get_template('index.html')
    context = {'temp' : description}
    return HttpResponse(template.render(context, request))

def random_layer(request):
    random_item = Layers.objects.all().order_by('?').first()
    description = random_item.layer_description
    template = loader.get_template('index.html')
    context = {'temp' : description}
    return HttpResponse(template.render(context, request))