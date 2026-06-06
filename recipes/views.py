from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from .models import Recipe, Category, Comment, Rating
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RecipeForm

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
    Handles comment submission for logged in users.
    """
    recipe = get_object_or_404(Recipe, slug=slug)
    comments = recipe.comments.all()
    avg_rating = recipe.ratings.aggregate(Avg("score"))["score__avg"]

    # Handle comment submission
    if request.method == "POST" and request.user.is_authenticated:
        body = request.POST.get("body")
        if body:
            Comment.objects.create(body=body, recipe=recipe, author=request.user)
            messages.success(request, "Comment added successfully!")
            return redirect("recipe_detail", slug=slug)

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


@login_required
def recipe_edit(request, slug):
    """
    Allow the recipe author to edit their own recipe.
    Redirects non-authors back to the recipe detail page.
    """
    recipe = get_object_or_404(Recipe, slug=slug)

    # Check ownership
    if recipe.author != request.user:
        messages.error(request, "You can only edit your own recipes!")
        return redirect("recipe_detail", slug=slug)

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, "Recipe updated successfully!")
            return redirect("recipe_detail", slug=recipe.slug)
    else:
        form = RecipeForm(instance=recipe)

    context = {
        "form": form,
        "recipe": recipe,
    }
    return render(request, "recipes/recipe_form.html", context)


@login_required
def recipe_delete(request, slug):
    """
    Allow the recipe author to delete their own recipe.
    Redirects non-authors back to the recipe detail page.
    """
    recipe = get_object_or_404(Recipe, slug=slug)

    # Check ownership
    if recipe.author != request.user:
        messages.error(request, "You can only delete your own recipes!")
        return redirect("recipe_detail", slug=slug)

    if request.method == "POST":
        recipe.delete()
        messages.success(request, "Recipe deleted successfully!")
        return redirect("home")

    context = {"recipe": recipe}
    return render(request, "recipes/recipe_confirm_delete.html", context)


@login_required
def comment_delete(request, comment_id):
    """
    Allow the comment author to delete their own comment.
    Redirects non-authors back to the recipe detail page.
    """
    comment = get_object_or_404(Comment, id=comment_id)

    # Check ownership
    if comment.author != request.user:
        messages.error(request, "You can only delete your own comments!")
        return redirect("recipe_detail", slug=comment.recipe.slug)

    if request.method == "POST":
        slug = comment.recipe.slug
        comment.delete()
        messages.success(request, "Comment deleted successfully!")
        return redirect("recipe_detail", slug=slug)

    context = {"comment": comment}
    return render(request, "recipes/comment_confirm_delete.html", context)


@login_required
def rate_recipe(request, slug):
    """
    Allow logged in users to rate a recipe out of 5 stars.
    Each user can only rate a recipe once - update_or_create
    ensures this by updating an existing rating if one exists.
    """
    recipe = get_object_or_404(Recipe, slug=slug)

    if request.method == "POST":
        score = request.POST.get("score")
        if score:
            Rating.objects.update_or_create(
                recipe=recipe, user=request.user, defaults={"score": score}
            )
            messages.success(request, "Rating saved successfully!")

    return redirect("recipe_detail", slug=slug)


@login_required
def profile(request):
    """
    Display the logged in user's profile page
    with all their posted recipes.
    """
    recipes = Recipe.objects.filter(author=request.user).annotate(
        avg_rating=Avg("ratings__score")
    )

    context = {"recipes": recipes}
    return render(request, "recipes/profile.html", context)


def custom_404(request, exception):
    """Custom 404 error page."""
    return render(request, "404.html", status=404)
