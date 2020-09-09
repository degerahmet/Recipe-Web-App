from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Recipe,Direction
# Create your views here.

def index(request):
    pass

def recipeid(request,recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(request,"recipebook/recipe.html",{
        "recipe" : recipe
    })
