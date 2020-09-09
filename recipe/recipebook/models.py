from django.db import models

# Create your models here.


class Ingredient(models.Model):
    quantitiy = models.CharField(max_length=255)                #1                      1/2
    measure = models.CharField(max_length=255,blank=True,null=True)            #blank                  cup
    name = models.CharField(max_length=255)                     #egg                    white sugar


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    specialname = models.CharField(max_length=255,blank=True,null=True)
    image = models.ImageField()
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient,blank=True,related_name="recipe")

    def __init__(self):
        self.specialname = str(self.name).casefold().strip().replace(" ","-")

class Directions(models.Model):
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE,related_name="directions")
    step = models.IntegerField()
    direction = models.TextField()
