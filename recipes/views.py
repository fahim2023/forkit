from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from .models import Recipe, Category, Comment, Rating

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


def recipe_detail(request, slug):
    """
    Display a single recipe with its comments and ratings.
    """
    recipe = get_object_or_404(Recipe, slug=slug)
    comments = recipe.comments.all()
    avg_rating = recipe.ratings.aggregate(Avg("score"))["score__avg"]

    context = {
        "recipe": recipe,
        "comments": comments,
        "avg_rating": avg_rating,
    }
    return render(request, "recipes/recipe_detail.html", context)
