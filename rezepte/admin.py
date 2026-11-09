from django.contrib import admin
from .models import Recipe, Category, RecipeIngredient, Ingredient


# Register your models here.
class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_at")
    list_filter = ("category",)
    inlines = [RecipeIngredientInline]


admin.site.register(Category)
admin.site.register(Ingredient)
