def display_menu(trainer):
	print(f"""
{trainer.name}, It is your turn. Select an action: 1-5.

(1) Attack
(2) Use potion
(3) Change Pokemon
(4) See players' stats
(5) Quit game
 """)


def execute_action(trainer, other_trainer, choice):
	while True:
		if choice == 1:
			trainer.attack_other_trainer(other_trainer)
			break
		if choice == 2:
			trainer.use_potion()
			break
		if choice == 3:
			print("\nThe method for this choice needs to be refactored.")
			# trainer.switch_active_pokemon(trainer)
			break
		if choice == 4:
			print()
			print(trainer)
			print()
			print(other_trainer)
			print("\nMake another selection.")
			choice = int(input("> "))