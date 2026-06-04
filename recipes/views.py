from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from .models import Recipe, Category, Comment, Rating
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
    categories = Category.objects.all()

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        category_id = request.POST.get("category")
        cooking_time = request.POST.get("cooking_time")
        servings = request.POST.get("servings")
        ingredients = request.POST.get("ingredients")
        instructions = request.POST.get("instructions")

        from django.utils.text import slugify

        slug = slugify(title)

        if Recipe.objects.filter(slug=slug).exists():
            slug = f"{slug}-{request.user.id}"

        recipe = Recipe.objects.create(
            title=title,
            slug=slug,
            description=description,
            category_id=category_id,
            cooking_time=cooking_time,
            servings=servings,
            ingredients=ingredients,
            instructions=instructions,
            author=request.user,
        )
        messages.success(request, "Recipe added successfully!")
        return redirect("recipe_detail", slug=recipe.slug)

    context = {"categories": categories}
    return render(request, "recipes/recipe_form.html", context)
