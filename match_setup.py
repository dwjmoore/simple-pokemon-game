import pokemon
import trainer


def create_pokemon():
	a = pokemon.Pokemon("Charmander", "Fire", 7)
	b = pokemon.Pokemon("Squirtle", "Water")
	c = pokemon.Pokemon("Lapras", "Water", 9)
	d = pokemon.Pokemon("Bulbasaur", "Grass", 10)
	e = pokemon.Pokemon("Vulpix", "Fire")
	f = pokemon.Pokemon("Staryu", "Water", 4)
	return [a, b, c, d, e, f]


def get_trainer_names():
	print(
	 "Welcome to the world of Pokemon.\nPlease enter a name for player one and hit enter."
	)
	trainer_one_name = input("> ")
	print(
	 f"\nHi, {trainer_one_name}! Welcome! Let's find you an opponent.\nEnter a name for the second player."
	)
	trainer_two_name = input("> ")
	print(f"\nHi, {trainer_two_name}! Welcome!\n")
	return trainer_one_name, trainer_two_name


def choose_pokemons(trainer_one_name, trainer_two_name, pokemon_list):
	trainer_one_pokemon = []
	trainer_two_pokemon = []

	print("\nLet's pick our Pokemon!\n")

	i = 0
	draft_round = 1

	while i < len(pokemon_list):
		if draft_round % 2 != 0:
			print(
			 f"{trainer_one_name}, would you like a Level {pokemon_list[i].level} {pokemon_list[i].name} or a Level {pokemon_list[i+1].level} {pokemon_list[i+1].name}?"
			)
			print(
			 f"{trainer_two_name} will get the other one. Type either '{pokemon_list[i].name}' or '{pokemon_list[i+1].name}'."
			)
			choice = input("> ")
			while choice != pokemon_list[i].name and choice != pokemon_list[i + 1].name:
				print(
				 f"Whoops, it looks like you didn't choose '{pokemon_list[i].name}' or '{pokemon_list[i+1].name}'. Try selecting one again!"
				)
				choice = input("> ")
			if choice == pokemon_list[i].name:
				trainer_one_pokemon.append(pokemon_list[i])
				trainer_two_pokemon.append(pokemon_list[i + 1])
			else:
				trainer_one_pokemon.append(pokemon_list[i + 1])
				trainer_two_pokemon.append(pokemon_list[i])
		else:
			print(
			 f"{trainer_two_name}, would you like a Level {pokemon_list[i].level} {pokemon_list[i].name} or a Level {pokemon_list[i+1].level} {pokemon_list[i+1].name}?"
			)
			print(
			 f"{trainer_one_name} will get the other one. Type either '{pokemon_list[i].name}' or '{pokemon_list[i+1].name}'."
			)
			choice = input("> ")
			while choice != pokemon_list[i].name and choice != pokemon_list[i + 1].name:
				print(
				 f"Whoops, it looks like you didn't choose '{pokemon_list[i].name}' or '{pokemon_list[i+1].name}'. Try selecting one again!"
				)
				choice = input("> ")
			if choice == pokemon_list[i].name:
				trainer_two_pokemon.append(pokemon_list[i])
				trainer_one_pokemon.append(pokemon_list[i + 1])
			else:
				trainer_two_pokemon.append(pokemon_list[i + 1])
				trainer_one_pokemon.append(pokemon_list[i])
		i += 2
		draft_round += 1

	trainer_one = trainer.Trainer(trainer_one_pokemon, 3, trainer_one_name)
	trainer_two = trainer.Trainer(trainer_two_pokemon, 3, trainer_two_name)

	return trainer_one, trainer_two