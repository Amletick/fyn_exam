from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'cooking_steps', 'cooking_time', 'image', 'ingredients']

    # Можно добавить дополнительные валидации или виджеты, если нужно
    cooking_time = forms.IntegerField(min_value=1, label="Cooking Time (in minutes)")
    ingredients = forms.CharField(widget=forms.Textarea, required=False)
