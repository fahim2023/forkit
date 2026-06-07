from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    """
    Represents a recipe category (e.g. Italian, Vegan, Desserts).
    Used to group and filter recipes on the homepage.
    """

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        """Return the category name as its string representation."""
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Recipe(models.Model):
    """
    Represents a recipe shared by a registered user.
    Contains all recipe details including ingredients, instructions,
    cooking time, servings, and an optional image.
    Linked to a Category and an author (User).
    """

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.IntegerField(help_text="Time in minutes")
    servings = models.IntegerField(default=4)
    image = models.ImageField(upload_to="recipes/", blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipes"
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="recipes"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return the recipe title as its string representation."""
        return self.title

    class Meta:
        ordering = ["-created_at"]


class Comment(models.Model):
    """
    Represents a comment left by a registered user on a recipe.
    Each comment is linked to both a Recipe and an author (User).
    Users can only delete their own comments.
    """

    body = models.TextField()
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a summary string showing the author and recipe."""
        return f"Comment by {self.author} on {self.recipe}"

    class Meta:
        ordering = ["-created_at"]


class Rating(models.Model):
    """
    Represents a star rating (1-5) given by a user to a recipe.
    The unique_together constraint ensures each user can only
    rate a recipe once. Used to calculate average recipe ratings.
    """

    score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ratings"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="ratings"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a summary string showing score, user and recipe."""
        return f"{self.score} stars by {self.user} on {self.recipe}"

    class Meta:
        unique_together = ("recipe", "user")
