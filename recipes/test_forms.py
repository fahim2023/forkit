from django.test import TestCase
from .forms import RecipeForm
from .models import Category


class TestRecipeForm(TestCase):
    """Tests for the RecipeForm."""

    def setUp(self):
        """Create test category."""
        self.category = Category.objects.create(
            name="Test Category", slug="test-category"
        )

    def test_form_is_valid(self):
        """Test form is valid with all required fields."""
        form = RecipeForm(
            {
                "title": "Test Recipe",
                "description": "A test description",
                "category": self.category.id,
                "cooking_time": 30,
                "servings": 4,
                "ingredients": "Test ingredients",
                "instructions": "Test instructions",
            }
        )
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_title_is_required(self):
        """Test that title field is required."""
        form = RecipeForm(
            {
                "title": "",
                "description": "A test description",
                "category": self.category.id,
                "cooking_time": 30,
                "servings": 4,
                "ingredients": "Test ingredients",
                "instructions": "Test instructions",
            }
        )
        self.assertFalse(
            form.is_valid(), msg="Title was not provided but form is valid"
        )

    def test_ingredients_is_required(self):
        """Test that ingredients field is required."""
        form = RecipeForm(
            {
                "title": "Test Recipe",
                "description": "A test description",
                "category": self.category.id,
                "cooking_time": 30,
                "servings": 4,
                "ingredients": "",
                "instructions": "Test instructions",
            }
        )
        self.assertFalse(
            form.is_valid(),
            msg="Ingredients was not provided but form is valid",
        )

    def test_instructions_is_required(self):
        """Test that instructions field is required."""
        form = RecipeForm(
            {
                "title": "Test Recipe",
                "description": "A test description",
                "category": self.category.id,
                "cooking_time": 30,
                "servings": 4,
                "ingredients": "Test ingredients",
                "instructions": "",
            }
        )
        self.assertFalse(
            form.is_valid(),
            msg="Instructions was not provided but form is valid",
        )
