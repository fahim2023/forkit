from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("recipe/create/", views.recipe_create, name="recipe_create"),
    path("recipe/<slug:slug>/", views.recipe_detail, name="recipe_detail"),
    path("recipe/<slug:slug>/edit/", views.recipe_edit, name="recipe_edit"),
]
