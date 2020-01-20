from rest_framework import serializers
from .models import Pokemon, PokemonStats


class PokemonStatsSerializer(serializers.ModelSerializer):
    stat_name = serializers.SerializerMethodField()

    class Meta:
        model = PokemonStats
        fields = ('base', 'stat_name')

    def get_stat_name(self, obj):
        return obj.stats_type.name


class PokemonPreevolutionSerializer(serializers.ModelSerializer):
    preevolution = serializers.SerializerMethodField()

    class Meta:
        model = Pokemon
        fields = ('id', 'name', 'preevolution')

    def get_preevolution(self, obj):
        if obj.pre_evolution is None:
            return None
        return PokemonPreevolutionSerializer(obj.pre_evolution).data


class PokemonEvolutionSerializer(serializers.ModelSerializer):
    evolutions = serializers.SerializerMethodField()

    class Meta:
        model = Pokemon
        fields = ('id', 'name', 'evolutions')

    def get_evolutions(self, obj):
        return PokemonEvolutionSerializer(obj.evolutions.all(), many=True).data


class PokemonSerializer(serializers.ModelSerializer):
    stats = serializers.SerializerMethodField()
    evolutions = serializers.SerializerMethodField()
    preevolution = serializers.SerializerMethodField()

    class Meta:
        model = Pokemon
        fields = ('id', 'name', 'height', 'weight', 'external_id', 'stats', 'evolutions', 'preevolution')

    def get_stats(self, obj):
        return PokemonStatsSerializer(obj.stats.all(), many=True).data

    def get_evolutions(self, obj):
        return PokemonEvolutionSerializer(obj.evolutions.all(), many=True).data

    def get_preevolution(self, obj):
        if obj.pre_evolution is None:
            return None
        return PokemonPreevolutionSerializer(obj.pre_evolution).data