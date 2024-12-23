from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Recipe, Category
from .forms import RecipeForm
from django.db.models import Q
import random
def home(request):
    all_recipes = list(Recipe.objects.all())
    recipes_count = len(all_recipes)
    
    if recipes_count < 5:
        recipes = all_recipes  # Если рецептов меньше 5, показываем все
    else:
        recipes = random.sample(all_recipes, 5)  # Если рецептов больше или равно 5, выбираем 5 случайных
    
    return render(request, 'home.html', {'recipes': recipes})



def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})


def add_edit_recipe(request, recipe_id=None):
    if recipe_id:
        recipe = get_object_or_404(Recipe, id=recipe_id)
    else:
        recipe = None

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            new_recipe = form.save()
            return redirect('recipe_detail', new_recipe.id)
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'add_edit_recipe.html', {'form': form, 'recipe': recipe})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def profile(request):
    recipes = Recipe.objects.filter(author=request.user)
    return render(request, 'profile.html', {'recipes': recipes})


def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        recipe.delete()
        return redirect('home')
    return render(request, 'confirm_delete_recipe.html', {'recipe': recipe})


def search(request):
    query = request.GET.get('q')
    if query:
        recipes = Recipe.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    else:
        recipes = Recipe.objects.all()
    
    return render(request, 'search_results.html', {'recipes': recipes, 'query': query})


def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})


def category_recipes(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    recipes = category.recipes.all()  # Все рецепты, относящиеся к категории
    return render(request, 'category_recipes.html', {'category': category, 'recipes': recipes})
