class Trainer:
	# A trainer has a list of pokemon, a number of potions and a name. When the trainer gets created, the first pokemon in their list of pokemons is the active pokemon (number 0)
	def __init__(self, pokemon_list, num_potions, name):
		self.pokemons = pokemon_list
		self.potions = num_potions
		self.current_pokemon = 0
		self.name = name

	def __repr__(self):
		# Prints the name of the trainer, the pokemon they currently have, and the current active pokemon.
		print("The trainer {name} has the following pokemon".format(name=self.name))
		for pokemon in self.pokemons:
			print(pokemon)
		return "The current active pokemon is {name}".format(
		 name=self.pokemons[self.current_pokemon].name)

	def switch_active_pokemon(self, new_active):
		# Switches the active pokemon to the number given as a parameter
		# First checks to see the number is valid (between 0 and the length of the list)
		if new_active < len(self.pokemons) and new_active >= 0:
			# You can't switch to a pokemon that is knocked out
			if self.pokemons[new_active].is_knocked_out:
				print(
				 "{name} is knocked out. You can't make it your active pokemon".format(
				  name=self.pokemons[new_active].name))
			# You can't switch to your current pokemon
			elif new_active == self.current_pokemon:
				print("{name} is already your active pokemon".format(
				 name=self.pokemons[new_active].name))
			# Switches the pokemon
			else:
				self.current_pokemon = new_active
				print("Go {name}, it's your turn!".format(
				 name=self.pokemons[self.current_pokemon].name))

	def use_potion(self):
		# Uses a potion on the active pokemon, assuming you have at least one potion.
		if self.potions > 0:
			print("You used a potion on {name}.".format(
			 name=self.pokemons[self.current_pokemon].name))
			# A potion restores 20 health
			self.pokemons[self.current_pokemon].gain_health(20)
			self.potions -= 1
		else:
			print("You don't have any more potions")

	def attack_other_trainer(self, other_trainer):
		# Your current pokemon attacks the other trainer's current pokemon
		my_pokemon = self.pokemons[self.current_pokemon]
		their_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
		my_pokemon.attack(their_pokemon)