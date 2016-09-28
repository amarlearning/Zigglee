from django.db import models
# from datetime import datetime
# from PIL import Image

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=250)
    ingredients = models.TextField(max_length=1500)
    recipe_intro = models.TextField(max_length=1500)
    cooking_method = models.TextField(max_length=15000)
    recipe_thumb = models.ImageField(upload_to="./zigglee/static/zigglee/uploads")
    cover_image = models.ImageField(upload_to="./zigglee/static/zigglee/uploads")
    visited = models.BigIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.recipe_name + " | visitor's count = " + str(self.visited)