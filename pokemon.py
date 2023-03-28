class Pokemon:
	def __init__(self, name, type, level=5):
		self.name = name
		self.level = level
		self.health = level * 5
		self.max_health = level * 5
		self.type = type
		self.is_knocked_out = False

	def __repr__(self):
		return "This level {level} {name} has {health} hit points remaining. They are a {type} type Pokemon".format(
		 level=self.level, name=self.name, health=self.health, type=self.type)

	def revive(self):
		# Reviving a pokemon will flip it's status to False
		self.is_knocked_out = False
		# A revived pokemon can't have 0 health. This is a safety precaution. revive() should only be called if the pokemon was given some health, but if it somehow has no health, its health gets set to 1.
		if self.health == 0:
			self.health = 1
		print("{name} was revived!".format(name=self.name))

	def knock_out(self):
		# Knocking out a pokemon will flip its status to True.
		self.is_knocked_out = True
		# A knocked out pokemon can't have any health. This is a safety precaution. knock_out() should only be called if heath was set to 0, but if somehow the pokemon had health left, it gets set to 0.
		if self.health != 0:
			self.health = 0
		print("{name} was knocked out!".format(name=self.name))

	def lose_health(self, amount):
		# Deducts heath from a pokemon and prints the current health reamining
		self.health -= amount
		if self.health <= 0:
			#Makes sure the health doesn't become negative. Knocks out the pokemon.
			self.health = 0
			self.knock_out()
		else:
			print("{name} now has {health} health.".format(name=self.name,
			                                               health=self.health))

	def gain_health(self, amount):
		# Adds to a pokemon's heath
		# If a pokemon goes from 0 heath, then revive it
		if self.health == 0:
			self.revive()
		self.health += amount
		# Makes sure the heath does not go over the max health
		if self.health >= self.max_health:
			self.health = self.max_health
		print("{name} now has {health} health.".format(name=self.name,
		                                               health=self.health))

	def attack(self, other_pokemon):
		# Checks to make sure the pokemon isn't knocked out
		if self.is_knocked_out:
			print(
			 "{name} can't attack because it is knocked out!".format(name=self.name))
			return
		# If the pokemon attacking has a disadvantage, then it deals damage equal to half its level to the other pokemon
		if (self.type == "Fire" and other_pokemon.type == "Water") or (
		  self.type == "Water"
		  and other_pokemon.type == "Grass") or (self.type == "Grass"
		                                         and other_pokemon.type == "Fire"):
			print("{my_name} attacked {other_name} for {damage} damage.".format(
			 my_name=self.name,
			 other_name=other_pokemon.name,
			 damage=round(self.level * 0.5)))
			print("It's not very effective")
			other_pokemon.lose_health(round(self.level * 0.5))
		# If the pokemon attacking has neither advantage or disadvantage, then it deals damage equal to its level to the other pokemon
		if (self.type == other_pokemon.type):
			print("{my_name} attacked {other_name} for {damage} damage.".format(
			 my_name=self.name, other_name=other_pokemon.name, damage=self.level))
			other_pokemon.lose_health(self.level)
		# If the pokemon attacking has advantage, then it deals damage equal to double its level to the other pokemon
		if (self.type == "Fire" and other_pokemon.type == "Grass") or (
		  self.type == "Water"
		  and other_pokemon.type == "Fire") or (self.type == "Grass"
		                                        and other_pokemon.type == "Water"):
			print("{my_name} attacked {other_name} for {damage} damage.".format(
			 my_name=self.name, other_name=other_pokemon.name, damage=self.level * 2))
			print("It's super effective")
			other_pokemon.lose_health(self.level * 2)