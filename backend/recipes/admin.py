from django.contrib import admin

from .models import (Favorite, Ingredient, Recipe, RecipeIngredient,
                     ShoppingList, Subscribe, Tag)


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    autocomplete_fields = ('ingredient',)
    extra = 1

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('ingredient')


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'author',
        'favorite_count',
        'tags_list',
        'cooking_time'
    )
    search_fields = (
        'name',
        'author__first_name',
        'author__last_name',
        'author__username',
    )
    list_filter = ('tags',)
    autocomplete_fields = ('author', 'tags',)
    inlines = [RecipeIngredientInline]

    def tags_list(self, obj):
        if tags := obj.tags.all():
            tags_list = ', '.join(tags.values_list('name', flat=True)[:2])
            if len(tags) > 2:
                tags_list += f' и еще {len(tags) - 2}'
            return tags_list
        return '-'

    tags_list.short_description = 'Теги'

    def favorite_count(self, obj):
        return Favorite.objects.filter(recipe=obj).distinct().count()

    favorite_count.short_description = 'Добавлений в избранное'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color',)
    search_fields = ('name', )


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit',)
    search_fields = ('name',)


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('user', 'author',)
    search_fields = ('user__first_name', 'user__last_name', 'user__username',
                     'author__first_name', 'author__last_name',
                     'author__username',)
    autocomplete_fields = ('user', 'author',)


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe',)
    search_fields = ('user__first_name', 'user__last_name', 'user__username',
                     'recipe__name',)
    autocomplete_fields = ('user',)
    raw_id_fields = ('recipe',)


@admin.register(ShoppingList)
class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe',)
    search_fields = ('user__first_name', 'user__last_name', 'user__username',
                     'recipe__name',)
    autocomplete_fields = ('user',)
    raw_id_fields = ('recipe',)
