from django.contrib import admin
from .models import Ingredient,Recipe,Direction
# Register your models here.

admin.site.site_header = 'Recipe Admin Dashboard'

class InlineDirection(admin.TabularInline):
    model = Direction
    extra = 1

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    
    list_display = ('name','description')
    fieldsets = (
        (None, {
            'fields' : (
                'name',
                'image',
                'description',
                'ingredients'
            )
        }),
    )
    inlines = [InlineDirection]


admin.site.register(Ingredient)
# admin.site.register(Direction)