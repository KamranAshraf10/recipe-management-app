from django.urls import path

from . import views

urlpatterns = [
    path("recipes/", views.recipes, name="recipes"),  # type: ignore
    path("update_recipe/<int:id>/", views.update_recipe, name="update_recipe"),
    path("delete_recipe/<int:id>/", views.delete_recipe, name="delete_recipe"),
]
