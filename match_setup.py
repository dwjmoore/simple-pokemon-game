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
	 "Welcome to the world of Pokemon. Please enter a name for player one and hit enter."
	)
	trainer_one_name = input()
	print(
	 f"Hi, {trainer_one_name}! Welcome! Let's find you an opponent. Enter a name for the second player."
	)
	trainer_two_name = input()
	print(f"Hi, {trainer_two_name}!")
	return trainer_one_name, trainer_two_name


def choose_pokemons(trainer_one_name, trainer_two_name, pokemon_list):
	trainer_one_pokemon = []
	trainer_two_pokemon = []

	print(
	 f"Let's pick our Pokemon! {trainer_one_name}, would you like a Level 7 Charmander, or a Level 7 Squirtle? {trainer_two_name} will get the other one. Type either 'Charmander' or 'Squirtle'."
	)
	choice = input()
	while choice != 'Charmander' and choice != 'Squirtle':
		print(
		 "Whoops, it looks like you didn't choose 'Charmander' or 'Squirtle'. Try selecting one again!"
		)
		choice = input()
	if choice == 'Charmander':
		trainer_one_pokemon.append(pokemon_list[0])
		trainer_two_pokemon.append(pokemon_list[1])
	else:
		trainer_one_pokemon.append(pokemon_list[1])
		trainer_two_pokemon.append(pokemon_list[0])

	print(
	 f"{trainer_two_name}, would you like a Level 9 Lapras, or a Level 10 Bulbasaur? {trainer_one_name} will get the other one. Type either 'Lapras' or 'Bulbasaur'."
	)
	choice = input()
	while choice != 'Lapras' and choice != 'Bulbasaur':
		print(
		 "Whoops, it looks like you didn't choose 'Lapras' or 'Bulbasaur'. Try selecting one again!"
		)
		choice = input()
	if choice == 'Lapras':
		trainer_one_pokemon.append(pokemon_list[3])
		trainer_two_pokemon.append(pokemon_list[2])
	else:
		trainer_one_pokemon.append(pokemon_list[2])
		trainer_two_pokemon.append(pokemon_list[3])

	print(
	 f"{trainer_one_name}, would you like a Level 5 Vulpix, or a Level 4 Staryu? {trainer_two_name} will get the other one. Type either 'Vulpix' or 'Staryu'."
	)
	choice = input()
	while choice != 'Vulpix' and choice != 'Staryu':
		print(
		 "Whoops, it looks like you didn't choose 'Vulpix' or 'Staryu'. Try selecting one again!"
		)
		choice = input()
	if choice == 'Vulpix':
		trainer_one_pokemon.append(pokemon_list[4])
		trainer_two_pokemon.append(pokemon_list[5])
	else:
		trainer_one_pokemon.append(pokemon_list[5])
		trainer_two_pokemon.append(pokemon_list[4])

	trainer_one = trainer.Trainer(trainer_one_pokemon, 3, trainer_one_name)
	trainer_two = trainer.Trainer(trainer_two_pokemon, 3, trainer_two_name)

	print("Let's get ready to fight! Here are our two trainers")

	# print(trainer_one)
	# print(trainer_two)

	return trainer_one, trainer_two