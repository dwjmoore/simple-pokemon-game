import match_setup
import match_actions

trainer_one_name, trainer_two_name = match_setup.get_trainer_names()

trainer_one, trainer_two = match_setup.choose_pokemons(
 trainer_one_name, trainer_two_name, match_setup.create_pokemon())

match_actions.display_menu(trainer_one)