# ForkIt

![ForkIt on all devices](documentation/images/amiresponsive.png)

[ForkIt](https://forkit-app-397f94f54229.herokuapp.com/) is a full-stack recipe sharing community built with Django, designed to bring together home cooks and food lovers. Users can discover, share and manage their own recipes whilst engaging with the community through comments and ratings.

[Click here to view the deployed site.](https://forkit-app-397f94f54229.herokuapp.com/)

---

## Table of Contents

- [Project Purpose](#project-purpose)
- [User Experience (UX)](#user-experience-ux)
  - [Goals and Objectives](#goals-and-objectives)
  - [User Stories](#user-stories)
  - [Wireframes](#wireframes)
- [Database Design](#database-design)
  - [ERD](#erd)
  - [Database Schema](#database-schema)
- [UI Design](#ui-design)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Imagery](#imagery)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Security Features](#security-features)
- [Deployment](#deployment)
- [Testing](#testing)
  - [Automated Testing](#automated-testing)
  - [Manual Testing](#manual-testing)
  - [Validator Testing](#validator-testing)
  - [Responsiveness](#responsiveness)
- [Bugs](#bugs)
- [Future Implementations](#future-implementations)
- [Credits](#credits)

---

## Project Purpose

ForkIt is a community-driven recipe sharing platform where registered users can post their own recipes, browse recipes shared by others, leave comments and rate dishes. The site provides value to home cooks looking for inspiration and to those wanting to share their culinary creations with a wider audience.

The site owner benefits by building an engaged food community and growing a valuable dataset of user-generated recipes.

---

## User Experience (UX)

### Goals and Objectives

**External user goals:**

- Browse and discover recipes shared by the community
- Share their own recipes with other food lovers
- Engage with other users through comments and ratings
- Manage their own content easily

**Site owner goals:**

- Build an engaged recipe sharing community
- Collect a valuable dataset of user-generated recipes
- Provide a platform that is intuitive and enjoyable to use

### User Stories

#### Site Visitor (not logged in)

- As a site visitor, I want to browse all recipes so that I can find cooking inspiration
- As a site visitor, I want to search recipes by keyword so that I can find specific dishes quickly
- As a site visitor, I want to filter recipes by category so that I can browse recipes relevant to my diet or mood
- As a site visitor, I want to view a full recipe detail page so that I can see ingredients and instructions
- As a site visitor, I want to register for an account so that I can share my own recipes

#### Registered User

- As a registered user, I want to log in to my account so that I can access my profile and recipes
- As a registered user, I want to add a new recipe so that I can share it with the community
- As a registered user, I want to upload an image with my recipe so that it looks appealing to other users
- As a registered user, I want to edit my own recipes so that I can correct mistakes or update them
- As a registered user, I want to delete my own recipes so that I can remove content I no longer want to share
- As a registered user, I want to leave a comment on a recipe so that I can share feedback with the author
- As a registered user, I want to delete my own comments so that I can remove something I posted
- As a registered user, I want to rate a recipe out of 5 stars so that I can help others decide what to cook
- As a registered user, I want to view my profile page so that I can see all my posted recipes in one place
- As a registered user, I want to log out securely so that my account is protected

#### Site Owner

- As the site owner, I want only logged-in users to add, edit or delete recipes so that content is managed responsibly
- As the site owner, I want users to only edit or delete their own content so that other users' recipes are protected
- As the site owner, I want an admin panel so that I can manage categories, users and recipes if needed
- As the site owner, I want the site to be fully responsive so that users on mobile devices have a good experience

### Wireframes

<details>
<summary>Homepage</summary>

![Wireframe of homepage](documentation/images/wireframes/wireframe-homepage.png)

</details>

<details>
<summary>Recipe Detail Page</summary>

![Wireframe of recipe detail page](documentation/images/wireframes/wireframe-recipe-detail.png)

</details>

<details>
<summary>Add Recipe Form</summary>

![Wireframe of add recipe form](documentation/images/wireframes/wireframe-add-recipe.png)

</details>

<details>
<summary>Profile Page</summary>

![Wireframe of profile page](documentation/images/wireframes/wireframe-profile.png)

</details>

<details>
<summary>Login / Register</summary>

![Wireframe of login page](documentation/images/wireframes/wireframe-login.png)

</details>

---

## Database Design

### ERD

_(Add ERD diagram image here)_

The application is built around five main entities:

- **User** — Django's built-in User model. A user can create many recipes, comments and ratings.
- **Category** — Groups recipes by cuisine or type (e.g. Italian, Vegan, Desserts).
- **Recipe** — Belongs to one user and one category. Can receive many comments and ratings.
- **Comment** — Belongs to one user and one recipe.
- **Rating** — A star rating (1-5) given by one user to one recipe. Each user can only rate a recipe once.

### Database Schema

| Model    | Field        | Type          | Notes       |
| -------- | ------------ | ------------- | ----------- |
| Category | name         | CharField     |             |
| Category | slug         | SlugField     | Unique      |
| Recipe   | title        | CharField     |             |
| Recipe   | slug         | SlugField     | Unique      |
| Recipe   | description  | TextField     |             |
| Recipe   | ingredients  | TextField     |             |
| Recipe   | instructions | TextField     |             |
| Recipe   | cooking_time | IntegerField  | Minutes     |
| Recipe   | servings     | IntegerField  | Default 4   |
| Recipe   | image        | ImageField    | Optional    |
| Recipe   | author       | ForeignKey    | to User     |
| Recipe   | category     | ForeignKey    | to Category |
| Recipe   | created_at   | DateTimeField | Auto        |
| Recipe   | updated_at   | DateTimeField | Auto        |
| Comment  | body         | TextField     |             |
| Comment  | recipe       | ForeignKey    | to Recipe   |
| Comment  | author       | ForeignKey    | to User     |
| Comment  | created_at   | DateTimeField | Auto        |
| Rating   | score        | IntegerField  | 1-5         |
| Rating   | recipe       | ForeignKey    | to Recipe   |
| Rating   | user         | ForeignKey    | to User     |
| Rating   | created_at   | DateTimeField | Auto        |

**Relationships:**

- A User can have many Recipes (one-to-many)
- A User can have many Comments (one-to-many)
- A User can have many Ratings (one-to-many)
- A Category can have many Recipes (one-to-many)
- A Recipe can have many Comments (one-to-many)
- A Recipe can have many Ratings (one-to-many)
- A User can only rate each Recipe once (enforced via unique_together)

---

## UI Design

### Colour Scheme

The colour scheme uses warm, food-inspired tones:

- **Terracotta (#C46438)** — primary actions, buttons, highlights
- **Olive Green (#58B783)** — accents, category badges
- **Cream (#FAF7F2)** — page background
- **Dark Brown (#2C1810)** — body text

These colours were chosen to evoke warmth and appetite, consistent with a food-focused platform.

### Typography

Bootstrap 5's default system font stack is used throughout for clean, readable text across all devices.

### Imagery

Food photography is sourced from [Pexels](https://www.pexels.com/) which provides free-to-use images. Users can upload their own recipe images via Cloudinary.

---

## Features

### Navigation

The navbar is fully responsive and collapses to a burger menu on mobile. It displays different links depending on the user's logged-in status:

- **Logged out:** Browse, Login, Register
- **Logged in:** Browse, Add Recipe, Profile, Logout

### Homepage

![Homepage](documentation/images/features/homepage-early.png)

Displays a hero section with a search bar and category filter buttons. Below, recipe cards are displayed in a responsive grid showing the recipe image, title, category, rating, cooking time and author.

### Search and Category Filter

![Category Filter](documentation/images/features/category-filter.png)

![Search Results](documentation/images/features/search-results.png)

Users can filter recipes by category using the filter buttons on the homepage. They can also search for recipes by keyword using the search bar.

### Recipe Detail Page

![Recipe Detail Page](documentation/images/features/recipe-detail-early.png)

Displays the full recipe including a large header image, category badge, title, description, cooking time, servings, rating and author. Ingredients are listed clearly and instructions are displayed as numbered steps. Logged in users can leave comments and rate the recipe. The recipe author sees Edit and Delete buttons.

### Add Recipe

![Add Recipe Form](documentation/images/features/add-recipe-form.png)

![Recipe Added Successfully](documentation/images/features/add-recipe-success.png)

A form allowing logged in users to submit a new recipe using Django's ModelForm with full validation. On successful submission the user is redirected to the new recipe's detail page with a success message displayed.

### Edit Recipe

![Edit Recipe Success](documentation/images/features/edit-recipe-success.png)

Logged in users can edit their own recipes using the same form as the create page, pre-populated with the existing recipe data. If a user attempts to edit another user's recipe they are redirected with an error message.

### Delete Recipe

![Delete Confirmation](documentation/images/features/delete-confirmation.png)

![Delete Success](documentation/images/features/delete-success.png)

A confirmation page is displayed before deleting a recipe to prevent accidental deletions. Only the recipe author can delete their own recipes.

### Comments

![Comment Added](documentation/images/features/comment-added.png)

![Comment Delete Confirmation](documentation/images/features/comment-delete-confirmation.png)

![Comment Deleted](documentation/images/features/comment-deleted.png)

Logged in users can leave comments on any recipe. The comment author sees a Delete button on their own comments. A confirmation page is displayed before deletion.

### Ratings

![Rating Success](documentation/images/features/rating-success.png)

Logged in users can rate any recipe they did not author out of 5 stars. Each user can only rate a recipe once. The average rating is displayed on both the homepage card and the recipe detail page.

### Profile Page

![Profile Page](documentation/images/features/profile-page.png)

Displays the logged in user's avatar, username and email. Below, all their posted recipes are shown in a card grid with View, Edit and Delete buttons.

### User Profile Page

![User Profile Page](documentation/images/features/user-profile-page.png)

Clicking "View Profile" on any recipe takes visitors to that user's public profile page showing all their posted recipes.

### Login / Register / Logout

![Login Page](documentation/images/features/login-page.png)

![Register Page](documentation/images/features/register-page.png)

![Logout Page](documentation/images/features/logout-page.png)

Custom authentication templates built with Django Allauth and Crispy Forms.

### Success Messages

![Success Message](documentation/images/features/auto-dismiss-message.png)

Django messages framework used throughout for feedback on all user actions. Messages automatically disappear after 3 seconds via a custom JavaScript function in `static/js/main.js`.

### Custom 404 Page

![Custom 404 Page](documentation/images/features/404-page.png)

A custom 404 page is displayed when a user navigates to a page that does not exist. Includes a link back to the homepage so users never need the browser's back button.

### Admin Panel

The Django admin panel allows the site owner to manage all recipes, categories, comments and ratings.

---

## Technologies Used

**Frontend:**

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

**Backend:**

- Python 3
- Django 6

**Database:**

- PostgreSQL (via Neon)

**Storage:**

- Cloudinary (media files)

**Deployment:**

- Heroku
- WhiteNoise (static files)
- Gunicorn (web server)

**Development Tools:**

- Git & GitHub (version control)
- VS Code
- Chrome DevTools
- [Base44](https://app.base44.com/) (wireframe design)

**Validation Tools:**

- [W3C HTML Validator](https://validator.w3.org/)
- [W3C CSS Validator (Jigsaw)](https://jigsaw.w3.org/css-validator/)
- [CI Python Linter](https://pep8ci.herokuapp.com/)
- Chrome Lighthouse / PageSpeed Insights
- [Amiresponsive](https://ui.dev/amiresponsive)

**Django Packages:**

- django-allauth
- django-crispy-forms
- crispy-bootstrap5
- Pillow
- dj-database-url
- psycopg2-binary
- cloudinary
- django-cloudinary-storage
- whitenoise
- gunicorn

---

## Security Features

- All secret keys and database URLs stored in environment variables (`env.py` locally, Heroku Config Vars in production)
- `env.py` is listed in `.gitignore` and never committed to the repository
- `DEBUG` is set to `False` in production via environment variable
- All recipe and comment edit/delete views protected with `@login_required`
- Users can only edit or delete their own content — ownership checked in every relevant view
- CSRF protection enabled on all forms
- `MESSAGE_TAGS` configured in `settings.py` to map Django message levels to Bootstrap alert classes

---

## Deployment

### Prerequisites

Ensure you have the following installed:

- Python 3
- pip
- Git

### Clone the Repository

```bash
git clone https://github.com/fahim2023/forkit
cd forkit
```

### Local Development Setup

1. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create an `env.py` file in the root directory:

```python
import os

os.environ["SECRET_KEY"] = "your-secret-key"
os.environ["DATABASE_URL"] = "your-database-url"
os.environ["CLOUDINARY_URL"] = "your-cloudinary-url"
os.environ["DEBUG"] = "True"
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Load initial category data:

```bash
python manage.py loaddata categories.json
```

> **Note:** Initial category data is stored as a fixture in `recipes/fixtures/categories.json`. Run this command any time the database is wiped to restore the default categories.

6. Create a superuser:

```bash
python manage.py createsuperuser
```

7. Run the development server:

```bash
python manage.py runserver
```

### Deploy to Heroku

1. Create a Heroku account at [heroku.com](https://heroku.com)
2. Install the Heroku CLI and log in:

```bash
heroku login
```

3. Create a new Heroku app:

```bash
heroku create your-app-name
```

4. Set config vars in Heroku:

```bash
heroku config:set SECRET_KEY='your-secret-key'
heroku config:set DATABASE_URL='your-database-url'
heroku config:set CLOUDINARY_URL='your-cloudinary-url'
```

5. Push to Heroku:

```bash
git push heroku main
```

6. Run migrations on Heroku:

```bash
heroku run python manage.py migrate
```

### Static Files

Static files are served using WhiteNoise. The `Procfile` includes a `release` command that runs `collectstatic` automatically on every deployment:

```
web: gunicorn forkit.wsgi
release: python manage.py collectstatic --noinput
```

---

## Testing

### Automated Testing

All automated tests were written using Django's built-in testing framework and use SQLite in memory for speed and isolation from the production database.

#### Form Tests

| Test                          | Description                         | Result | Screenshot                                                                  |
| ----------------------------- | ----------------------------------- | ------ | --------------------------------------------------------------------------- |
| test_form_is_valid            | Form valid with all required fields | Pass   | ![](documentation/images/testing/test-forms-pass.png)                       |
| test_title_is_required        | Form invalid without title          | Pass   | ![](documentation/images/testing/test-forms-title-required-pass.png)        |
| test_ingredients_is_required  | Form invalid without ingredients    | Pass   | ![](documentation/images/testing/test-forms-ingredients-required-pass.png)  |
| test_instructions_is_required | Form invalid without instructions   | Pass   | ![](documentation/images/testing/test-forms-instructions-required-pass.png) |

#### View Tests

| Test                                | Description                                       | Result | Screenshot                                                                   |
| ----------------------------------- | ------------------------------------------------- | ------ | ---------------------------------------------------------------------------- |
| test_home_page_loads                | Homepage loads with correct template              | Pass   | ![](documentation/images/testing/test-views-home-pass.png)                   |
| test_recipe_detail_loads            | Recipe detail page loads correctly                | Pass   | ![](documentation/images/testing/test-views-recipe-detail-pass.png)          |
| test_recipe_create_requires_login   | Unauthenticated users redirected from create page | Pass   | ![](documentation/images/testing/test-views-create-login-required-pass.png)  |
| test_recipe_create_logged_in        | Logged in users can access create page            | Pass   | ![](documentation/images/testing/test-views-create-logged-in-pass.png)       |
| test_profile_requires_login         | Unauthenticated users redirected from profile     | Pass   | ![](documentation/images/testing/test-views-profile-login-required-pass.png) |
| test_recipe_edit_requires_ownership | Non-authors cannot edit recipes                   | Pass   | ![](documentation/images/testing/test-views-edit-ownership-pass.png)         |
| test_search_functionality           | Search returns relevant recipes                   | Pass   | ![](documentation/images/testing/test-views-search-pass.png)                 |
| test_category_filter                | Category filter returns relevant recipes          | Pass   | ![](documentation/images/testing/test-views-category-filter-pass.png)        |

![All tests passing](documentation/images/testing/all-tests-pass.png)

### Manual Testing

Manual testing was carried out throughout the development process. Each feature was tested after implementation and a final round of testing was completed on the deployed Heroku site.

| User Story         | Test                              | Expected Result        | Actual Result             | Pass/Fail | Screenshot                                                     |
| ------------------ | --------------------------------- | ---------------------- | ------------------------- | --------- | -------------------------------------------------------------- |
| Browse all recipes | Navigate to homepage              | Recipe grid displays   | Recipes shown             | Pass      | ![](documentation/images/features/homepage-early.png)          |
| Search recipes     | Type "Carbonara" in search        | Matching recipes shown | Carbonara displayed       | Pass      | ![](documentation/images/features/search-results.png)          |
| Filter by category | Click "Italian"                   | Italian recipes shown  | Italian recipes displayed | Pass      | ![](documentation/images/features/category-filter.png)         |
| View recipe detail | Click View Recipe                 | Full recipe page loads | Detail page loads         | Pass      | ![](documentation/images/features/recipe-detail-early.png)     |
| Register account   | Fill register form                | Account created        | Account created           | Pass      | ![](documentation/images/features/register-page.png)           |
| Log in             | Enter credentials                 | Redirected to homepage | Login successful          | Pass      | ![](documentation/images/features/login-page.png)              |
| Add recipe         | Fill add recipe form              | Recipe created         | Recipe created            | Pass      | ![](documentation/images/features/add-recipe-success.png)      |
| Edit own recipe    | Click Edit on own recipe          | Changes saved          | Recipe updated            | Pass      | ![](documentation/images/features/edit-recipe-success.png)     |
| Delete own recipe  | Click Delete and confirm          | Recipe removed         | Recipe deleted            | Pass      | ![](documentation/images/features/delete-success.png)          |
| Leave a comment    | Type and submit comment           | Comment appears        | Comment posted            | Pass      | ![](documentation/images/features/comment-added.png)           |
| Delete own comment | Click Delete on comment           | Comment removed        | Comment deleted           | Pass      | ![](documentation/images/features/comment-deleted.png)         |
| Rate a recipe      | Select stars and submit           | Rating saved           | Rating saved              | Pass      | ![](documentation/images/features/rating-success.png)          |
| View profile       | Click Profile in navbar           | Profile page loads     | Profile loads             | Pass      | ![](documentation/images/features/profile-page.png)            |
| Log out            | Click Logout and confirm          | Session ended          | Logged out                | Pass      | ![](documentation/images/features/logout-page.png)             |
| Login required     | Access /recipe/create/ logged out | Redirected to login    | Redirected                | Pass      | ![](documentation/images/features/login-required-redirect.png) |
| Edit ownership     | Try to edit another user's recipe | Error message shown    | Error displayed           | Pass      | ![](documentation/images/features/edit-ownership-error.png)    |
| Custom 404         | Navigate to non-existent URL      | Custom 404 shown       | 404 page shown            | Pass      | ![](documentation/images/features/404-page.png)                |
| Success messages   | Perform any CRUD action           | Message auto-dismisses | Message dismisses         | Pass      | ![](documentation/images/features/auto-dismiss-message.png)    |

### Validator Testing

#### HTML Validation

All HTML pages were validated using the [W3C Markup Validator](https://validator.w3.org/).

| Page          | Result | Screenshot                                                       |
| ------------- | ------ | ---------------------------------------------------------------- |
| Homepage      | Pass   | ![](documentation/images/validation/html-homepage-pass.png)      |
| Recipe Detail | Pass   | ![](documentation/images/validation/html-recipe-detail-pass.png) |
| Add Recipe    | Pass   | ![](documentation/images/validation/html-add-recipe-pass.png)    |
| Edit Recipe   | Pass   | ![](documentation/images/validation/html-edit-recipe-pass.png)   |
| Delete Recipe | Pass   | ![](documentation/images/validation/html-delete-pass.png)        |
| Profile       | Pass   | ![](documentation/images/validation/html-profile-pass.png)       |
| Login         | Pass   | ![](documentation/images/validation/html-login-pass.png)         |
| Register      | Pass   | ![](documentation/images/validation/html-signup-pass.png)        |
| Logout        | Pass   | ![](documentation/images/validation/html-logout-pass.png)        |
| 404 Page      | Pass   | ![](documentation/images/validation/html-404-pass.png)           |

#### CSS Validation

CSS was validated using the [W3C Jigsaw Validator](https://jigsaw.w3.org/css-validator/).

| File      | Result           | Screenshot                                        |
| --------- | ---------------- | ------------------------------------------------- |
| style.css | Pass - No errors | ![](documentation/images/validation/css-pass.png) |

> Note: 10 warnings were shown relating to CSS custom variables which the validator cannot statically check. These are not errors and do not affect the validity of the CSS.

#### Python PEP8 Validation

All Python files were validated using the [CI Python Linter](https://pep8ci.herokuapp.com/).

| File            | Result | Screenshot                                                     |
| --------------- | ------ | -------------------------------------------------------------- |
| views.py        | Pass   | ![](documentation/images/validation/pep8-views-pass.png)       |
| models.py       | Pass   | ![](documentation/images/validation/pep8-models-pass.png)      |
| forms.py        | Pass   | ![](documentation/images/validation/pep8-forms-pass.png)       |
| admin.py        | Pass   | ![](documentation/images/validation/pep8-admin-pass.png)       |
| recipes/urls.py | Pass   | ![](documentation/images/validation/pep8-urls-pass.png)        |
| settings.py     | Pass   | ![](documentation/images/validation/pep8-settings-pass.png)    |
| forkit/urls.py  | Pass   | ![](documentation/images/validation/pep8-forkit-urls-pass.png) |

#### Lighthouse

| Page          | Device  | Performance | Accessibility | Best Practices | SEO | Screenshot                                                                |
| ------------- | ------- | ----------- | ------------- | -------------- | --- | ------------------------------------------------------------------------- |
| Homepage      | Desktop | 94          | 94            | 100            | 91  | ![](documentation/images/lighthouse/lighthouse-homepage-desktop.png)      |
| Homepage      | Mobile  | 77          | 83            | 100            | 91  | ![](documentation/images/lighthouse/lighthouse-homepage-mobile.png)       |
| Recipe Detail | Desktop | 95          | 93            | 100            | 91  | ![](documentation/images/lighthouse/lighthouse-recipe-detail-desktop.png) |
| Recipe Detail | Mobile  | 84          | 84            | 100            | 91  | ![](documentation/images/lighthouse/lighthouse-recipe-detail-mobile.png)  |
| Profile       | Desktop | 99          | 95            | 100            | 98  | ![](documentation/images/lighthouse/lighthouse-profile-desktop.png)       |
| Profile       | Mobile  | 95          | 88            | 100            | 98  | ![](documentation/images/lighthouse/lighthouse-profile-mobile.png)        |

### Responsiveness

Tested on the following devices and browsers:

| Device  | Browser | Result |
| ------- | ------- | ------ |
| Desktop | Chrome  | Pass   |
| Desktop | Firefox | Pass   |
| Desktop | Safari  | Pass   |
| Tablet  | Chrome  | Pass   |
| Mobile  | Chrome  | Pass   |
| Mobile  | Safari  | Pass   |

---

## Bugs

### Bug 1 — Pillow not installed

- **Issue:** `ImageField` requires Pillow but it was not in the initial dependencies, causing a `SystemCheckError` on `makemigrations`
- **Fix:** Ran `pip install Pillow` and updated `requirements.txt`
- **Screenshot:** ![Bug 1](documentation/images/bugs/pillow_issue.png)

### Bug 2 — NoReverseMatch for recipe_create and profile URLs

- **Issue:** `base.html` referenced `{% url 'recipe_create' %}` and `{% url 'profile' %}` before these URL patterns had been created, causing a `NoReverseMatch` error on every page load
- **Fix:** Replaced unbuilt URLs with `#` placeholders in `base.html` until the views and URLs were created incrementally
- **Screenshot:** ![Bug 2](documentation/images/bugs/bug-02-noreversematch.png)

### Bug 3 — URL ordering caused 404 on recipe create page

- **Issue:** `recipe/create/` was being matched by `recipe/<slug:slug>/` pattern because the slug URL was defined first. Django treated "create" as a slug and threw a 404
- **Fix:** Moved `recipe/create/` above `recipe/<slug:slug>/` in `urls.py`
- **Screenshot:** ![Bug 3](documentation/images/bugs/bug-03-url-ordering.png)

### Bug 4 — Error messages not displaying correct colour

- **Issue:** Django's `messages.error` uses the tag `error` but Bootstrap uses `danger` for red alerts
- **Fix:** Added `MESSAGE_TAGS` to `settings.py` to map Django message levels to Bootstrap CSS classes
- **Screenshot:** ![Bug 4](documentation/images/bugs/bug-04-message-tags.png)

### Bug 5 — Footer not sticking to bottom of page

- **Issue:** Footer was floating in the middle of the page when there was not enough content to fill the viewport height
- **Fix:** Added Bootstrap flex utilities — `d-flex flex-column min-vh-100` on body, `flex-grow-1` on main and `mt-auto` on footer
- **Screenshot:** ![Bug 5](documentation/images/bugs/bug-05-footer.png)

### Bug 6 — Comment submission not working

- **Issue:** Comment submission code was missing from the `recipe_detail` view
- **Fix:** Added POST request handling to `recipe_detail` view
- **Screenshot:** ![Bug 6](documentation/images/bugs/bug-06-comments-not-submitting.png)

### Bug 7 — Custom 404 page not displaying locally

- **Issue:** Custom 404 page was not displaying because `DEBUG=True` locally overrides custom error pages
- **Fix:** Custom 404 pages only show when `DEBUG=False` — confirmed working on Heroku
- **Screenshot:** ![Bug 7](documentation/images/bugs/bug-07-404-page.png)

### Bug 8 — Static files not loading on Heroku

- **Issue:** CSS and Bootstrap styles not loading on Heroku because `staticfiles/` was in `.gitignore` and collectstatic had never been run
- **Fix:** Added a `release` command to `Procfile` so collectstatic runs automatically on every deploy
- **Screenshot:** ![Bug 8](documentation/images/bugs/bug-08-static-files.png)

### Bug 9 — Cloudinary images not uploading to Heroku

- **Issue:** Images not being sent to Cloudinary because `DEFAULT_FILE_STORAGE` is deprecated in Django 6
- **Fix:** Replaced with the new Django `STORAGES` dictionary setting
- **Before:** ![Bug 9 before](documentation/images/bugs/bug-09-cloudinary-before.png)
- **After:** ![Bug 9 after](documentation/images/bugs/bug-09-cloudinary-after.png)

### Bug 10 — collectstatic copying 0 files

- **Issue:** `cloudinary_storage` was listed before `django.contrib.staticfiles` in `INSTALLED_APPS`, causing it to intercept the static files collection process
- **Fix:** Moved `cloudinary_storage` to after `django.contrib.staticfiles`
- **Screenshot:** ![Bug 10](documentation/images/bugs/bug-10-collectstatic.png)

### Bug 11 — PEP8 line too long in views.py

- **Issue:** Line 53 in `views.py` was 81 characters, exceeding PEP8 limit of 79
- **Fix:** Split `Comment.objects.create()` across multiple lines and added `pyproject.toml` to configure Black
- **Before:** ![PEP8 error](documentation/images/validation/pep8-views-error.png)
- **After:** ![PEP8 pass](documentation/images/validation/pep8-views-pass.png)

### Bug 12 — PEP8 errors in models.py

- **Issue:** 5 lines in `models.py` exceeded 79 characters due to long ForeignKey definitions
- **Fix:** Split the long lines across multiple lines
- **Before:** ![PEP8 models error](documentation/images/validation/pep8-models-error.png)
- **After:** ![PEP8 models pass](documentation/images/validation/pep8-models-pass.png)

### Bug 13 — PEP8 errors in forms.py

- **Issue:** 3 lines in `forms.py` exceeded 79 characters due to long placeholder text strings
- **Fix:** Split long strings using Python's implicit string concatenation
- **Before:** ![PEP8 forms error](documentation/images/validation/pep8-forms-error.png)
- **After:** ![PEP8 forms pass](documentation/images/validation/pep8-forms-pass.png)

### Bug 14 — PEP8 errors in urls.py

- **Issue:** Lines 9 and 11 in `recipes/urls.py` exceeded 79 characters
- **Fix:** Split the long path definitions across multiple lines
- **Before:** ![PEP8 urls error](documentation/images/validation/pep8-urls-error.png)
- **After:** ![PEP8 urls pass](documentation/images/validation/pep8-urls-pass.png)

### Bug 15 — PEP8 errors in settings.py

- **Issue:** Multiple lines exceeded 79 characters and had trailing whitespace in `AUTH_PASSWORD_VALIDATORS`
- **Fix:** Split validator class names across multiple lines and used VS Code "Trim Trailing Whitespace"
- **Before:** ![Settings error](documentation/images/validation/pep8-settings-error-long.png)
- **After:** ![Settings pass](documentation/images/validation/pep8-settings-pass.png)

### Bug 16 — HTML heading hierarchy error on homepage

- **Issue:** `h5` heading in recipe cards was skipping from `h1` to `h5`
- **Fix:** Changed `h5` to `h2` with Bootstrap `h5` class to maintain visual styling
- **Before:** ![HTML error](documentation/images/validation/html-homepage-error.png)
- **After:** ![HTML pass](documentation/images/validation/html-homepage-pass.png)

### Bug 17 — HTML heading hierarchy errors in recipe detail page

- **Issue:** Multiple heading hierarchy errors throughout the recipe detail template
- **Fix:** Changed all headings to correct semantic levels using Bootstrap classes to maintain appearance
- **Before:** ![Error](documentation/images/validation/html-recipe-detail-error1.png)
- **After:** ![Pass](documentation/images/validation/html-recipe-detail-pass.png)

### Bug 18 — Missing h1 heading on login, signup and logout pages

- **Issue:** The login, signup and logout pages had no `h1` heading, triggering HTML validator warnings
- **Fix:** Changed `h2` to `h1` with Bootstrap `h2` class on all three pages
- **Before:** ![Login warning](documentation/images/validation/html-login-warning.png)
- **After:** ![Login pass](documentation/images/validation/html-login-pass.png)

### Bug 19 — HTML heading hierarchy errors on profile pages

- **Issue:** Profile pages had missing `h1` headings and incorrect heading hierarchy
- **Fix:** Changed username heading to `h1`, "My Recipes" to `h2`, and recipe card titles to `h3`
- **Before:** ![Profile warning](documentation/images/validation/html-profile-warning.png)
- **After:** ![Profile pass](documentation/images/validation/html-profile-pass.png)

### Bug 20 — Automated test failing due to required category field

- **Issue:** `test_form_is_valid` was failing because `category` is a required ForeignKey but no category was being created in test data
- **Fix:** Added a `setUp` method to create a test `Category` object and passed its ID to the form data
- **Before:** ![Test fail](documentation/images/testing/test-forms-fail.png)
- **After:** ![Test pass](documentation/images/testing/test-forms-pass.png)

---

## Future Implementations

- Favorites/bookmarking system for saving recipes
- Recipe print functionality
- Pagination for the recipe grid
- Social sharing buttons
- Reply to comments functionality
- Password reset via email

---

## Credits

### Content

- Recipe content and sample data written by myself.

### Media

- Food photography sourced from [Pexels](https://www.pexels.com/) (free to use licence)

### Code

- Django documentation — [docs.djangoproject.com](https://docs.djangoproject.com/)
- Bootstrap 5 documentation — [getbootstrap.com](https://getbootstrap.com/)
- Django Allauth documentation — [django-allauth.readthedocs.io](https://django-allauth.readthedocs.io/)
- Code Institute Django walkthrough (CodeStar Blog) — used as reference for project structure and configuration patterns

### Tools

- [Favicon.io](https://favicon.io/) — favicon generation
- [Amiresponsive](https://ui.dev/amiresponsive) — responsiveness screenshots
- [Neon](https://neon.tech/) — PostgreSQL database hosting
- [Cloudinary](https://cloudinary.com/) — media file storage

### Acknowledgements

- Code Institute for the course content and support
