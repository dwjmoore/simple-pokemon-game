import pokemon
import trainer

a = pokemon.Pokemon("Charmander", "Fire", 7)
b = pokemon.Pokemon("Squirtle", "Water")
c = pokemon.Pokemon("Lapras", "Water", 9)
d = pokemon.Pokemon("Bulbasaur", "Grass", 10)
e = pokemon.Pokemon("Vulpix", "Fire")
f = pokemon.Pokemon("Staryu", "Water", 4)

#Getting input to get the trainers names and letting them select the Pokemon they want.
trainer_one_name = input(
 "Welcome to the world of Pokemon. Please enter a name for player one and hit enter. "
)
trainer_two_name = input(
 "Hi, " + str(trainer_one_name) +
 "! Welcome! Let's find you an opponent. Enter a name for the second player. ")

choice = input(
 "Hi, " + trainer_two_name + "! Let's pick our Pokemon! " + trainer_one_name +
 ", would you like a Level 7 Charmander, or a Level 7 Squirtle? " +
 trainer_two_name +
 " will get the other one. Type either 'Charmander' or 'Squirtle'. ")

while choice != 'Charmander' and choice != 'Squirtle':
	choice = input(
	 "Whoops, it looks like you didn't choose 'Charmander' or 'Squirtle'. Try selecting one again! "
	)

# Keeping track of which pokemon they chose
trainer_one_pokemon = []
trainer_two_pokemon = []

if choice == 'Charmander':
	trainer_one_pokemon.append(a)
	trainer_two_pokemon.append(b)

else:
	trainer_one_pokemon.append(b)
	trainer_two_pokemon.append(a)

# Selecting the second pokemon
choice = input(
 trainer_two_name +
 ", would you like a Level 9 Lapras, or a Level 10 Bulbasaur? " +
 trainer_one_name +
 " will get the other one. Type either 'Lapras' or 'Bulbasaur'. ")

while choice != 'Lapras' and choice != 'Bulbasaur':
	choice = input(
	 "Whoops, it looks like you didn't choose 'Lapras' or 'Bulbasaur'. Try selecting one again! "
	)

if choice == 'Lapras':
	trainer_one_pokemon.append(d)
	trainer_two_pokemon.append(c)

else:
	trainer_one_pokemon.append(c)
	trainer_two_pokemon.append(d)

# Selecting the third pokemon
choice = input(trainer_one_name +
               ", would you like a Level 5 Vulpix, or a Level 4 Staryu? " +
               trainer_two_name +
               " will get the other one. Type either 'Vulpix' or 'Staryu'. ")

while choice != 'Vulpix' and choice != 'Staryu':
	choice = input(
	 "Whoops, it looks like you didn't choose 'Vulpix' or 'Staryu'. Try selecting one again! "
	)

if choice == 'Vulpix':
	trainer_one_pokemon.append(e)
	trainer_two_pokemon.append(f)

else:
	trainer_one_pokemon.append(f)
	trainer_two_pokemon.append(e)

# Creating the Trainer objects with the given names and pokemon lists
trainer_one = trainer.Trainer(trainer_one_pokemon, 3, trainer_one_name)
trainer_two = trainer.Trainer(trainer_two_pokemon, 3, trainer_two_name)

print("Let's get ready to fight! Here are our two trainers")

print(trainer_one)
print(trainer_two)

# Testing attacking, giving potions, and switching pokemon. This could be built out more to ask for input
trainer_one.attack_other_trainer(trainer_two)
trainer_two.attack_other_trainer(trainer_one)
trainer_two.use_potion()
trainer_one.attack_other_trainer(trainer_two)
trainer_two.switch_active_pokemon(0)
trainer_two.switch_active_pokemon(1)