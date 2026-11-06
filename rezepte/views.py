from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms import RecipeForm

# Create your views here.


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "rezepte/recipe_list.html", {"recipes": recipes})


def recipe_create(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            return redirect("recipe_detail", slug=recipe.slug)
    else:
        form = RecipeForm()
    return render(request, "rezepte/recipe_form.html", {"form": form})


def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    return render(request, "rezepte/recipe_detail.html", {"recipe": recipe})


def recipe_update(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("recipe_detail", slug=recipe.slug)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, "rezepte/recipe_form.html", {"form": form, "recipe": recipe})


def recipe_delete(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    if request.method == "POST":
        recipe.delete()
        return redirect("recipe_list")
    return render(request, "rezepte/recipe_confirm_delete.html", {"recipe": recipe})
