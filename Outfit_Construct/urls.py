from django.urls import path

from Outfit_Construct import views
urlpatterns = [
    path("Outfit_Construct/", views.home, name = "home"),
    path("Outfit_Construct/closet", views.createPage, name = "createPage"),
    path("Outfit_Construct/clothing", views.selected_clothing, name = "selected_clothing"),
    path("Outfit_Construct/clothing/home", views.clothing_home, name = "clothing_home"),
    path("Outfit_Construct/clothing/edit", views.edit_clothing, name = "edit_clothing"),
    path("Outfit_Construct/clothing/create", views.create_clothing, name = "create_clothing"),
    path("Outfit_Construct/clothing/delete", views.delete_clothing, name = "delete_clothing"),

    path("Outfit_Construct/palette", views.selected_palette, name = "selected_palette"),
    path("Outfit_Construct/palette/home", views.palette_home, name = "palette_home"),

    path("Outfit_Construct/drawer", views.selected_drawer, name = "selected_drawer"),

    path("Outfit_Construct/random/drawer", views.random_drawer, name = "random_drawer"),
    path("Outfit_Construct/random/clothes", views.random_clothes, name = "random_clothes"),
    path("Outfit_Construct/random/colour", views.random_colour, name = "random_colour"),
    path("Outfit_Construct/random/hexcode", views.random_hexcode, name = "random_hexcode"),
    path("Outfit_Construct/random/palette", views.random_palette, name = "random_palette"),
    path("Outfit_Construct/random/palette_list", views.random_palette_list, name = "random_list"),
    path("Outfit_Construct/random/layer", views.random_layer, name = "random_layer"),
]