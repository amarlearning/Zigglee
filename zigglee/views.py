from django.shortcuts import render
from django.http import Http404
from .models import Recipe
import re

# Create your views here.
def index(request):
    all_recipe = Recipe.objects.all()
    context = {
        'all_recipes' : all_recipe,
    }
    return render(request, 'zigglee/index.html', context)

def detail(request, recipe_id):
    try:
        selected_recipe = Recipe.objects.get(pk=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404("This page Does Not Exist")
    else:
        ingredients = re.split(',', selected_recipe.ingredients)
        return render(request, 'zigglee/detail.html', {
            'recipe' : selected_recipe,
            'ingredients' : ingredients,
        })