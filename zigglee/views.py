from django.shortcuts import render
from django.http import Http404
from .models import Recipe
import re

# Create your views here.
def index(request):
    all_recipe = Recipe.objects.all()
    most_viewed = Recipe.objects.all().order_by('-visited')[:3]
    context = {
        'all_recipes' : all_recipe,
        'most_viewed' : most_viewed,
    }
    return render(request, 'zigglee/index.html', context)

def list(request):
    all_recipe = Recipe.objects.all()
    context = {
        'all_recipe' : all_recipe,
    }
    return render(request, 'zigglee/recipelist.html', context)

def about(request):
    return render(request, 'zigglee/about.html')

def contact(request):
    return render(request, 'zigglee/contact.html')

def detail(request, recipe_id):
    try:
        selected_recipe = Recipe.objects.get(pk=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404("This page Does Not Exist")
    else:
        ingredients = re.split(',', selected_recipe.ingredients)
        selected_recipe.visited += 1
        selected_recipe.save()
        return render(request, 'zigglee/detail.html', {
            'recipe' : selected_recipe,
            'ingredients' : ingredients,
        })
