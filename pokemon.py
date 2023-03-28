class Pokemon:

	def __init__(self, name, type, level=5):
		self.name = name
		self.level = level
		self.health = level * 5
		self.max_health = level * 5
		self.type = type
		self.is_knocked_out = False

	def __repr__(self):
		return f"This level {self.level} {self.name} has {self.health} hit points remaining. They are a {self.type} type Pokemon"

	def revive(self):
		self.is_knocked_out = False
		if self.health == 0:
			self.health = 1
		print(f"{self.name} was revived!")

	def knock_out(self):
		self.is_knocked_out = True
		if self.health != 0:
			self.health = 0
		print(f"{self.name} was knocked out!")

	def lose_health(self, amount):
		self.health -= amount
		if self.health <= 0:
			self.health = 0
			self.knock_out()
		else:
			print(f"{self.name} now has {self.health} health.")

	def gain_health(self, amount):
		if self.health == 0:
			self.revive()
		self.health += amount
		if self.health >= self.max_health:
			self.health = self.max_health
		print(f"{self.name} now has {self.health} health.")

	def attack(self, other_pokemon):
		if self.is_knocked_out:
			print(f"{self.name} can't attack because it is knocked out!")
			return

		if ((self.type == "Fire" and other_pokemon.type == "Water")
		    or (self.type == "Water" and other_pokemon.type == "Grass")
		    or (self.type == "Grass" and other_pokemon.type == "Fire")):
			print(
			 f"{self.name} attacked {other_pokemon.name} for {round(self.level * 0.5)} damage."
			)
			print("It's not very effective")
			other_pokemon.lose_health(round(self.level * 0.5))

		if (self.type == other_pokemon.type):
			print(f"{self.name} attacked {other_pokemon.name} for {self.level} damage.")
			other_pokemon.lose_health(self.level)

		if ((self.type == "Fire" and other_pokemon.type == "Grass")
		    or (self.type == "Water" and other_pokemon.type == "Fire")
		    or (self.type == "Grass" and other_pokemon.type == "Water")):
			print(
			 f"{self.name} attacked {other_pokemon.name} for {self.level * 2} damage.")
			print("It's super effective")
			other_pokemon.lose_health(self.level * 2)