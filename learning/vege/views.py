from django.shortcuts import render
from .models import *

# Create your views here.
def recipes(request):
    if request.method == "POST":
        data = request.POST

        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        Recipe.objects.create(
            recipe_image = recipe_image,
            recipe_name = recipe_name,
            recipe_description = recipe_description
        )

    context = {'page' : 'Upload recipes'}       
    
    return render(request, 'recipe/recipe.html', context)