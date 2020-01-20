from django.core.management.base import BaseCommand, CommandError
from ...services import get_evolution_chains, save_pokemon_info


class Command(BaseCommand):
    help = 'Import a evolution chain from pokeapi.co'

    def add_arguments(self, parser):
        parser.add_argument('evolution_id', type=int)

    def handle(self, *args, **options):
        self.stdout.write("... getting info of the evolution chain")
        try:
            evolution_info = get_evolution_chains(options.get('evolution_id'))
        except ValueError:
            raise CommandError(f"the evolution not found")

        self.stdout.write("... saving info in the database")
        save_pokemon_info(evolution_info.get("chain"))

        self.stdout.write(self.style.SUCCESS("DONE. The evolution chain was saved."))