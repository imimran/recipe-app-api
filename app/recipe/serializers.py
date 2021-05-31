from django.core import files
from django.db.models import fields
from django.db.models.query import QuerySet
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from core.models import Tag, Ingredient, Recipe


class TagSerializer(serializers.ModelSerializer):
    """ Serializer for Tag Object """

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id', )


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for an ingredient object"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for an Recipe object"""
    ingredients = serializers.PrimaryKeyRelatedField(many=True, queryset=Ingredient.objects.all())
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())

    class Meta:
        model = Recipe
        fields = '__all__'
        read_only_fields = ('id',)


class RecipeDetailsSerializer(RecipeSerializer):
    """ For Recipe Details """
    ingredients = IngredientSerializer(many=True, read_only = True)
    tags = TagSerializer(many=True, read_only = True)


class RecipeImageUploadSerializer(serializers.ModelSerializer):
    """Serializer for upload image"""

    class Meta:
        model = Recipe
        fields = ('id', 'image')
        read_only_fields = ('id',)

