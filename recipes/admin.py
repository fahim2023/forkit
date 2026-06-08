# Admin configuration for ForkIt models
from django.contrib import admin
from .models import Category, Recipe, Comment, Rating


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin configuration for Category model."""

    # Auto-populate slug field from name
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "slug")


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Admin configuration for Recipe model."""

    # Auto-populate slug field from title
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author", "category", "created_at")
    list_filter = ("category",)
    search_fields = ("title", "description")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin configuration for Comment model."""

    list_display = ("author", "recipe", "created_at")


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Admin configuration for Rating model."""

    list_display = ("user", "recipe", "score")
