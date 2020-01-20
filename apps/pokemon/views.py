from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import Pokemon
from .serializers import PokemonSerializer


class PokemonDetailsAPIView(GenericAPIView):
    queryset = Pokemon.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            pokemon = Pokemon.objects.get(name=kwargs.get('name'))
        except:
            return Response({"message": "pokemon not found"}, 400)

        return Response(PokemonSerializer(pokemon).data, 200)