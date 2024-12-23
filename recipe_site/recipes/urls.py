from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/add/', views.add_edit_recipe, name='add_recipe'),
    path('recipe/edit/<int:recipe_id>/', views.add_edit_recipe, name='edit_recipe'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('recipe/delete/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    path('search/', views.search, name='search'),
    path('categories/', views.categories, name='categories'),
    path('category/<int:category_id>/', views.category_recipes, name='category_recipes'),
]
