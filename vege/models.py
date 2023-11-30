from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to="recipe")
    
    def __str__(self):
        return f"The name of recipe is {self.recipe_name} and it details {self.recipe_description}"