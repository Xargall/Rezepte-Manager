from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Recipe, Category
from .forms import RecipeForm

# Create your views here.


class RecipeListView(ListView):
    model = Recipe
    template_name = "rezepte/recipe_list.html"
    context_object_name = "recipes"

    def get_queryset(self):
        queryset = Recipe.objects.all()
        category_name = self.request.GET.get("category")
        if category_name:
            queryset = queryset.filter(category__name=category_name)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "rezepte/recipe_detail.html"
    context_object_name = "recipe"
    slug_field = "slug"
    slug_url_kwarg = "slug"


def recipe_create(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            return redirect("recipe_detail", slug=recipe.slug)
    else:
        form = RecipeForm()
    return render(request, "rezepte/recipe_form.html", {"form": form})


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
