from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("recipe/create/", views.recipe_create, name="recipe_create"),
    path("recipe/<slug:slug>/", views.recipe_detail, name="recipe_detail"),
    path("recipe/<slug:slug>/edit/", views.recipe_edit, name="recipe_edit"),
    path("recipe/<slug:slug>/delete/", views.recipe_delete, name="recipe_delete"),
    path(
        "comment/<int:comment_id>/delete/", views.comment_delete, name="comment_delete"
    ),
    path("recipe/<slug:slug>/rate/", views.rate_recipe, name="rate_recipe"),
    path("profile/", views.profile, name="profile"),
]
