class Trainer:

	def __init__(self, pokemon_list, num_potions, name):
		self.pokemons = pokemon_list
		self.potions = num_potions
		self.active_pokemon = 0
		self.name = name

	def __repr__(self):
		print(f"The trainer {self.name} has the following pokemon")
		for pokemon in self.pokemons:
			print(pokemon)
		return f"The current active pokemon is {self.pokemons[self.active_pokemon].name}"

	def switch_active_pokemon(self, new_active):
		if new_active < len(self.pokemons) and new_active >= 0:
			if self.pokemons[new_active].is_knocked_out:
				print(
				 f"{self.pokemons[new_active].name} is knocked out. You can't make it your active pokemon"
				)
			elif new_active == self.active_pokemon:
				print(f"{self.pokemons[new_active].name} is already your active pokemon")
			else:
				self.active_pokemon = new_active
				print(f"Go {self.pokemons[self.active_pokemon].name}, it's your turn!")

	def use_potion(self):
		if self.potions > 0:
			print(f"You used a potion on {self.pokemons[self.active_pokemon].name}.")
			self.pokemons[self.active_pokemon].gain_health(20)
			self.potions -= 1
		else:
			print("You don't have any more potions")

	def attack_other_trainer(self, other_trainer):
		my_pokemon = self.pokemons[self.active_pokemon]
		their_pokemon = other_trainer.pokemons[other_trainer.active_pokemon]
		my_pokemon.attack(their_pokemon)
