from django.db import models


class Pokemon(models.Model):
    name = models.CharField(null=False, max_length=100)
    height = models.DecimalField(max_digits=6, decimal_places=2)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    external_id = models.PositiveIntegerField(null=False)
    pre_evolution = models.ForeignKey('pokemon.Pokemon', related_name="evolutions", null=True, on_delete=models.SET_NULL)


class StatsType(models.Model):
    name = models.CharField(null=False, max_length=100)


class PokemonStats(models.Model):
    stats_type = models.ForeignKey('pokemon.StatsType', null=False, on_delete=models.CASCADE)
    pokemon = models.ForeignKey('pokemon.Pokemon', related_name='stats', null=False, on_delete=models.CASCADE)
    base = models.PositiveIntegerField(null=False)