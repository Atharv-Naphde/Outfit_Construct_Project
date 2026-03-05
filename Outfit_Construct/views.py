from django.http import HttpResponse,Http404
from django.shortcuts import render
from django.template import loader
from Outfit_Construct.models import Drawers, Clothes, Colours, Hexcodes, Palette, PaletteList, Layers
from django import forms
#User creation and editing forms
class clothesForm (forms.ModelForm):
    cloth_id = forms.IntegerField()
    drawer_id = forms.ModelChoiceField(queryset=Drawers.objects.all(), required=False)
    layer_id = forms.ModelChoiceField(queryset=Layers.objects.all(), required=False)
    colour = forms.ModelChoiceField(queryset=Colours.objects.all())
    hexcode = forms.ModelChoiceField(queryset=Hexcodes.objects.all())
    item_type = forms.CharField()
    cloth_description = forms.CharField(initial='')
    class Meta:
        model = Clothes
        fields = "__all__"  # or list fields explicitly for security
       # exclude = ['cloth_id']

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
    #placeholder_link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    placeholder_link = "4"
    context = {
        'temp' : temp,
        'cloth1_link' : cloth1.cloth_id,
        'cloth1_name' : cloth1.cloth_description,
        'cloth2_link' : cloth2.cloth_id,
        'cloth2_name' : cloth2.cloth_description,
        'cloth3_link' : cloth3.cloth_id,
        'cloth3_name' : cloth3.cloth_description,

        'palette1_link' : palette1.palette_id,
        'palette1_name' : palette1.palette_description,
        'palette2_link' : palette2.palette_id,
        'palette2_name' : palette2.palette_description,
        'palette3_link' : palette3.palette_id,
        'palette3_name' : palette3.palette_description,
    }
    return HttpResponse(template.render(context, request))

def edit_clothing(request):
    template = loader.get_template('edit_clothing.html')
    context = {}
    return HttpResponse(template.render(context, request))

def create_clothing(request):
    template = loader.get_template('create_clothing.html')
    form = clothesForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        """
        #print(Drawers.objects.get(drawer_id = 1))
        #print(Drawers.objects.get(drawer_id=1).drawer_id)
        drawer_id = request.POST.get("drawer_id")
        layer_id = request.POST.get("layer_id")
        colour = request.POST.get("colour")
        hexcode = request.POST.get("hexcode")
        item_type = request.POST.get("item_type")
        cloth_description = request.POST.get("cloth_description")
        #temp = Clothes.objects.get(drawer_id = request.POST.get("drawer_id"))
        Clothes.objects.raw("insert into clothes (drawer_id , layer_id, colour, hexcode, item_type, cloth_description) values ("+drawer_id+" , "+layer_id+" , "+colour+" , "+hexcode+" , "+item_type+" , "+cloth_description+")")
        #print(temp[0].cloth_description)
        
        Clothes.objects.create(
            #cloth_id=str(request.POST.get("cloth_id")),
            drawer_id = str(request.POST.get("drawer_id")),
            layer_id=str(request.POST.get("layer_id")),
            colour = str(request.POST.get("colour")),
            hexcode = str(request.POST.get("hexcode")),
            item_type = str(request.POST.get("item_type")),
            cloth_description = str(request.POST.get("cloth_description")),
        )
        """
    context = {'form': form}
    return HttpResponse(template.render(context, request))

def outfit_suggest(cloth_id):
    #input cloth id, output a list of clothes that match the selected piece of clothing.
    cloth_details = Clothes.objects.raw("select * from clothes where cloth_id = '" + cloth_id + "'")
    cloth_colour = str(cloth_details[0].colour_id)
    cloth_layer = str(cloth_details[0].layer_id_id)
    cloth_type = str(cloth_details[0].item_type)
    valid_layers = Layers.objects.raw("select  * from layers where layer_id != '"+cloth_layer+"'")
    palette_query = PaletteList.objects.raw("select * from main.palette_list where colour = '" + cloth_colour + "'")
    valid_palette_id = []
    i = 0
    while i in range(len(palette_query)):
        valid_palette_id.append(palette_query[i].palette_id_id)
        i = i+1

    valid_colours = []
    for palette_ids in valid_palette_id:
        colour_query = PaletteList.objects.raw("select colour, palette_list_id from main.palette_list where palette_id = '"+palette_ids+"'")
        i = 0
        while i in range(len(colour_query)):
            if colour_query[i].colour_id not in valid_colours:
                valid_colours.append(colour_query[i].colour_id)
            i = i + 1
    list_of_colours = ""
    for colours in valid_colours:
        list_of_colours += "colour = '" + colours + "' or "
    list_of_colours = list_of_colours[:-4]
    # list_of_colours += "hexcode = '#FFFFFF'"

    valid_clothes = Clothes.objects.raw("select * from clothes where ("+list_of_colours+") and (item_type != '"+cloth_type+"' or layer_id != '"+cloth_layer+"')")
    #print("Output of the outfit suggest function : ")
    #print(valid_clothes)
    return valid_clothes

def selected_palette(request):
    template = loader.get_template('selected_colour.html')
    if request.GET.get('palette_id'):
        palette_id = request.GET.get('palette_id')
    else:
        palette_id = "1"
    palette_query = Palette.objects.raw("select  * from palette where palette_id = '"+palette_id+"'")
    colours = PaletteList.objects.raw("select * from main.palette_list where palette_id = '"+palette_id+"'")
    random_palette = Palette.objects.all().order_by('?')
    palette1 = random_palette[0]
    palette2 = random_palette[1]
    palette3 = random_palette[2]
    context = {
        "palette_description" : palette_query[0].palette_description,
        "colours" : colours,
        'palette1_link': palette1.palette_id,
        'palette1_name': palette1.palette_description,
        'palette2_link': palette2.palette_id,
        'palette2_name': palette2.palette_description,
        'palette3_link': palette3.palette_id,
        'palette3_name': palette3.palette_description,

    }
    return HttpResponse(template.render(context, request))

def selected_clothing(request):
    template = loader.get_template('selected_clothing.html')
    if request.GET.get('cloth_id'):
        cloth_id = request.GET.get('cloth_id')
    else:
        cloth_id = "1"
    cloth_query = Clothes.objects.raw("select * from clothes where cloth_id = '"+cloth_id+"'")
    cloth = cloth_query[0]
    drawer_query = Drawers.objects.raw("select * from main.drawers where drawer_id = '"+str(cloth.drawer_id_id)+"'")
    drawer = drawer_query[0].drawer_description
    layer_query = Layers.objects.raw("select * from main.layers where layer_id = '"+str(cloth.layer_id_id)+"'")
    layer = layer_query[0].layer_description
    #The code for image cannot be tested as the images are not currently in the database.
    image="Placeholder image"
    palette_query = PaletteList.objects.raw("select * from main.palette_list where colour = '"+str(cloth.colour_id)+"'")
    palette_name = Palette.objects.raw(
        "select * from main.palette where palette_id = '" + str(palette_query[0].palette_id_id) + "'")
    palettes = palette_name[0].palette_description
    """
    #This code should be implemented if a colour is in multiple palettes. The code is tested and is functional.
    palettes = []
    for query_id in range(len(palette_query)):
        palette_name = Palette.objects.raw("select * from main.palette where palette_id = '"+str(palette_query[query_id].palette_id_id)+"'")
        palettes.append(str(palette_name[0].palette_description))
    """
    #outfit suggestions returns a raw query set containing all outfit recommendations.
    outfit_suggestions = []
    outfit_suggestions = outfit_suggest(cloth_id)
    context = {
        'cloth_description' : cloth.cloth_description,
        'colour' : cloth.colour_id,
        'hexcode' : cloth.hexcode_id,
        'drawer' : drawer,
        'layer' : layer,
        'item_type': cloth.item_type,
        'image' : image,
        'palettes' : palettes,
        'outfit_suggestions' : outfit_suggestions,
               }
    return HttpResponse(template.render(context, request))


def createPage(request):
    template = loader.get_template('testing.html')
    #clothes_mapping = {'cloth_description': 'cloth_description',}
    # clothes = Clothes.objects.raw("Select clothes.cloth_id, clothes.cloth_description from main.clothes")
    clothes = Clothes.objects.raw("Select clothes.cloth_id, clothes.cloth_description, layers.layer_description, clothes.layer_id from main.clothes join main.layers using (layer_id)") #test this
    #translations=clothes_mapping
    #temp = Clothes.objects.raw("Select * from main.clothes")
    context = {
        'cloth' : clothes
    }
    #for p in Clothes.objects.raw("Select clothes.cloth_id, layers.layer_description, clothes.cloth_description, clothes.hexcode, clothes.colour, clothes.drawer_id from clothes join layers where clothes.layer_id = layers.layer_id"):
        #print(p)
    return HttpResponse(template.render(context, request))

def createPage2(request):
    template = loader.get_template('create.html')
    random_clothes = Clothes.objects.all().order_by('?')
    cloth1 = random_clothes[0]
    cloth2 = random_clothes[1]
    cloth3 = random_clothes[2]
    random_palette = Palette.objects.all().order_by('?')
    palette1 = random_palette[0]
    palette2 = random_palette[1]
    palette3 = random_palette[2]
    temp = "Temp Function"
    placeholder_link = "4"
    context = {
        'temp': temp,
        'cloth1_link': placeholder_link,
        'cloth1_name': cloth1.cloth_description,
        'cloth2_link': placeholder_link,
        'cloth2_name': cloth2.cloth_description,
        'cloth3_link': placeholder_link,
        'cloth3_name': cloth3.cloth_description,

        'palette1_link': placeholder_link,
        'palette1_name': palette1.palette_description,
        'palette2_link': placeholder_link,
        'palette2_name': palette2.palette_description,
        'palette3_link': placeholder_link,
        'palette3_name': palette3.palette_description,
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