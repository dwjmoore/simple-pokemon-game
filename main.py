import match_setup
import match_actions

trainer_one_name, trainer_two_name = match_setup.get_trainer_names()

trainer_one, trainer_two = match_setup.choose_pokemons(
 trainer_one_name, trainer_two_name, match_setup.create_pokemon())

print("\nLet's get ready to fight! Here are our two trainers\n")
print(trainer_one)
print()
print(trainer_two)

while True:
	match_actions.display_menu(trainer_one)
	trainer_one_choice = int(input("> "))
	if trainer_one_choice == 5:
		break
	match_actions.execute_action(trainer_one, trainer_two, trainer_one_choice)

	match_actions.display_menu(trainer_two)
	trainer_two_choice = int(input("> "))
	if trainer_two_choice == 5:
		break
	match_actions.execute_action(trainer_two, trainer_one, trainer_two_choice)

print("\nThanks for playing. Good bye!")