from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
# Create your views here.

def recipes(request):
    if request.method == "POST":
        data = request.POST

        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")

        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image,
        )

        return redirect("recipes")

    queryset = Recipe.objects.all()
    context = {"recipes": queryset}

    return render(request,"vege/recipes.html", context)


def update_recipe(request, id):
    
    queryset = Recipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST

        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")
    
        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description
        
        if recipe_image:
            queryset.recipe_image = recipe_image
        
        queryset.save()
        return redirect("recipes")

    context = {"recipe": queryset}
    return render(request,"vege/recipes.html", context)
    

def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect("recipes")