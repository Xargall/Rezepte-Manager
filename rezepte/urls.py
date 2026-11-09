from django.urls import path
from . import views

urlpatterns = [
    path("", views.RecipeListView.as_view(), name="recipe_list"),
    path("rezepte/neu/", views.recipe_create, name="recipe_create"),
    path(
        "rezepte/<slug:slug>/", views.RecipeDetailView.as_view(), name="recipe_detail"
    ),
    path("rezepte/<slug:slug>/bearbeiten", views.recipe_update, name="recipe_update"),
    path("rezepte/<slug:slug>/loeschen/", views.recipe_delete, name="recipe_delete"),
]
