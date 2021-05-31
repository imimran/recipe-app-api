from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import Serializer

from core.models import Tag, Ingredient, Recipe

from . import serializers


class TagViewSet(viewsets.GenericViewSet, 
                mixins.ListModelMixin,
                mixins.CreateModelMixin):
    """Manage Tag in DB"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

    def get_queryset(self):
        """ Return objects for current auth user only """
        return self.queryset.filter(user=self.request.user).order_by('-name')


    def perform_create(self, serializer):
        """ Create a new Tag """
        serializer.save(user=self.request.user)   

class IngredientViewSet(viewsets.GenericViewSet, 
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin):
    """Manage ingredients in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')


    def perform_create(self, serializer):
        """ Create a new Ingredient """
        serializer.save(user=self.request.user) 


class RecipeViewSet(viewsets.ModelViewSet):
    """ Manage Recipe """
    queryset = Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Return Recipe for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user)


    def get_serializer_class(self):
        """Return appropiate serializer class"""
        if self.action == 'retrieve':
            return serializers.RecipeDetailsSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """ Create a new auth recipe """
        serializer.save(user=self.request.user) 
