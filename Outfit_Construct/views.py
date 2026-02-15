from django.http import HttpResponse,Http404
from django.shortcuts import render
from django.template import loader
from Outfit_Construct.models import Drawers, Clothes, Colours, Hexcodes, Palette, PaletteList, Layers


# Create your views here.
def home(request):
    template = loader.get_template('index.html')
    temp = "Temp Function"
    context = {'temp' : temp}
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
    context = {'temp' : description}
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