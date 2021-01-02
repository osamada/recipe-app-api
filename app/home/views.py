from django.shortcuts import render
from django.contrib.auth.models import User
from recipe.serializers import TagSerializer
from core.models import Tag, Ingredient, Recipe
# Create your views here.
def HomeView(request):
    return render(request, 'home/home.html',)

def CreateView(request, pk=None):
    tags = Tag.objects.all()
    ingr = Ingredient.objects.all()
    args = {'Tag':tags, 'Ing': ingr}
    return render(request, 'home/create.html', args)

def ListView(request):
    recipes = Recipe.objects.all()
    args = {'recp':recipes}
    return render(request, 'home/list.html', args)
