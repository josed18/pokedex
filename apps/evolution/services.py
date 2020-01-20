from ..pokemon.models import PokemonStats, StatsType, Pokemon
import requests


def get_evolution_chains(evolution_chain_id):
    r = requests.get(f"https://pokeapi.co/api/v2/evolution-chain/{evolution_chain_id}/")
    if r.status_code not in [200, 201]:
        raise ValueError
    return r.json()


def get_pokemon_info(pokemon_name):
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/")
    if r.status_code not in [200, 201]:
        raise ValueError
    return r.json()


def save_pokemon_info(pokemon_evolution_info, pre_evolution_id=None):
    try:
        pokemon_data = get_pokemon_info(pokemon_evolution_info.get('species', {}).get('name'))
    except ValueError:
        return None

    pokemon = Pokemon.objects.create(
        name=pokemon_data.get("name"),
        height=pokemon_data.get("height", 0)/10,
        weight=pokemon_data.get("weight", 0)/10,
        external_id=pokemon_data.get("id"),
        pre_evolution_id=pre_evolution_id,
    )

    for stats in pokemon_data.get("stats", []):
        stats_type, created = StatsType.objects.get_or_create(name=stats.get('stat', {}).get('name'))

        pokemon_stats = PokemonStats.objects.create(
            stats_type=stats_type,
            pokemon=pokemon,
            base=stats.get('base_stat'),
        )

    for evolution_info in pokemon_evolution_info.get('evolves_to', []):
        save_pokemon_info(evolution_info, pokemon.id)

    return pokemon
