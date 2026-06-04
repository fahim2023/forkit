from django.shortcuts import render

from django.db.models import Avg, Q
from .models import Recipe, Category

# Create your views here.


def home(request):
    """
    Display the homepage with all recipes.
    Supports search by keyword and filtering by category.
    """
    recipes = Recipe.objects.all().annotate(avg_rating=Avg("ratings__score"))
    categories = Category.objects.all()

    context = {
        "recipes": recipes,
        "categories": categories,
    }
    return render(request, "recipes/home.html", context)
