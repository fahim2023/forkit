from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Recipe, Category


class TestRecipeViews(TestCase):
    """Tests for the recipe views."""

    def setUp(self):
        """Set up test data."""
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.category = Category.objects.create(name="Italian", slug="italian")
        self.recipe = Recipe.objects.create(
            title="Test Recipe",
            slug="test-recipe",
            description="A test description",
            ingredients="Test ingredients",
            instructions="Test instructions",
            cooking_time=30,
            servings=4,
            author=self.user,
            category=self.category,
        )

    def test_home_page_loads(self):
        """Test homepage loads successfully."""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/home.html")

    def test_recipe_detail_loads(self):
        """Test recipe detail page loads successfully."""
        response = self.client.get(
            reverse("recipe_detail", args=["test-recipe"])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/recipe_detail.html")

    def test_recipe_create_requires_login(self):
        """Test that recipe create redirects unauthenticated users."""
        response = self.client.get(reverse("recipe_create"))
        self.assertEqual(response.status_code, 302)

    def test_recipe_create_logged_in(self):
        """Test that logged in users can access recipe create page."""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("recipe_create"))
        self.assertEqual(response.status_code, 200)

    def test_profile_requires_login(self):
        """Test that profile page redirects unauthenticated users."""
        response = self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, 302)

    def test_recipe_edit_requires_ownership(self):
        """Test that non-authors cannot edit a recipe."""
        other_user = User.objects.create_user(
            username="otheruser", password="testpass123"
        )
        self.client.login(username="otheruser", password="testpass123")
        response = self.client.get(
            reverse("recipe_edit", args=["test-recipe"])
        )
        self.assertEqual(response.status_code, 302)

    def test_search_functionality(self):
        """Test that search returns relevant results."""
        response = self.client.get(reverse("home") + "?q=Test")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test Recipe", response.content)

    def test_category_filter(self):
        """Test that category filter returns relevant results."""
        response = self.client.get(reverse("home") + "?category=italian")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test Recipe", response.content)
