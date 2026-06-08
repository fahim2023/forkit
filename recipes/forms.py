# Forms for creating and editing recipes

from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    """
    Form for creating and editing recipes.
    Excludes author and slug as these are set automatically.
    """

    class Meta:
        model = Recipe
        fields = [
            "title",
            "description",
            "category",
            "cooking_time",
            "servings",
            "ingredients",
            "instructions",
            "image",
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. Grandma's Pasta",
                }
            ),
            "description": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "A brief tagline for your recipe",
                }
            ),
            "category": forms.Select(attrs={"class": "form-select"}),
            "cooking_time": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "30"}
            ),
            "servings": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "4"}
            ),
            "ingredients": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": (
                        "200g spaghetti\n4 egg yolks\n" "100g pecorino..."
                    ),
                }
            ),
            "instructions": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": (
                        "Boil pasta in salted water\n"
                        "Whisk eggs with cheese..."
                    ),
                }
            ),
            "image": forms.FileInput(
                attrs={"class": "form-control", "accept": "image/*"}
            ),
        }
