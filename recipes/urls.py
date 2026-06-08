# URL patterns for the recipes application
from django.urls import path
from . import views

urlpatterns = [
    # Home page - browse and search recipes
    path("", views.home, name="home"),
    # Recipe CRUD operations
    path("recipe/create/", views.recipe_create, name="recipe_create"),
    path("recipe/<slug:slug>/", views.recipe_detail, name="recipe_detail"),
    path("recipe/<slug:slug>/edit/", views.recipe_edit, name="recipe_edit"),
    path(
        "recipe/<slug:slug>/delete/", views.recipe_delete, name="recipe_delete"
    ),
    # Comment operations
    path(
        "comment/<int:comment_id>/delete/",
        views.comment_delete,
        name="comment_delete",
    ),
    # Rating operations
    path("recipe/<slug:slug>/rate/", views.rate_recipe, name="rate_recipe"),
    # User profile pages
    path("profile/", views.profile, name="profile"),
    path("profile/<str:username>/", views.user_profile, name="user_profile"),
]
