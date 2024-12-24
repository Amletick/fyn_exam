from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    cooking_steps = models.TextField()
    cooking_time = models.PositiveIntegerField()  # Время приготовления в минутах
    image = models.ImageField(upload_to='recipes/images/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    ingredients = models.TextField(null=True, blank=True)  # Например, список ингредиентов

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)  # Описание категории, если нужно

    def __str__(self):
        return self.title
    
class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='categories')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='recipes')

    order = models.PositiveIntegerField(default=0) 

    class Meta:
        unique_together = ('recipe', 'category')  

    def __str__(self):
        return f"{self.recipe.title} - {self.category.title}"
