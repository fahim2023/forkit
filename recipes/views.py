from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from .models import Recipe, Category, Comment, Rating
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from forms import RecipeForm

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


@login_required
def recipe_create(request):
    """
    Allow logged in users to create a new recipe.
    Redirects to recipe detail page on success.
    """
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            from django.utils.text import slugify

            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.slug = slugify(recipe.title)
            if Recipe.objects.filter(slug=recipe.slug).exists():
                recipe.slug = f"{recipe.slug}-{request.user.id}"
            recipe.save()
            messages.success(request, "Recipe added successfully!")
            return redirect("recipe_detail", slug=recipe.slug)
    else:
        form = RecipeForm()

    context = {"form": form}
    return render(request, "recipes/recipe_form.html", context)
