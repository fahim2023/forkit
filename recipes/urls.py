from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("recipe/<slug:slug>/", views.recipe_detail, name="recipe_detail"),
    path("recipe/create/", views.recipe_create, name="recipe_create"),
]
