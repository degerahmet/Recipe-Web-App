from django.db import models

# Create your models here.


class Ingredient(models.Model):
    quantitiy = models.CharField(max_length=255)                #1                      1/2
    measure = models.CharField(max_length=255,blank=True,null=True)            #blank                  cup
    name = models.CharField(max_length=255)                     #egg                    white sugar
    def __str__(self):
        if self.measure is None:
            return f"{self.quantitiy} {self.name}"
        return f"{self.quantitiy} {self.measure} of {self.name}"
    

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient,blank=True,related_name="recipe")

    def __str__(self):
        return self.name
    
    # def __init__(self):
    #     self.specialname = str(self.name).casefold().strip().replace(" ","-")

class Direction(models.Model):
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE,related_name="directions")
    step = models.IntegerField()
    direction = models.TextField()

    def __str__(self):
        return f"{self.step}. {self.direction} for {self.recipe.name}"
    
