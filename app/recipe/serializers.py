from django.core import files
from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from core.models import Tag, Ingredient


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
