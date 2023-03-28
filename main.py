import match_setup

trainer_one, trainer_two = match_setup.choose_pokemons(match_setup.get_trainer_names(), match_setup.create_pokemon())

print()
print(trainer_one)
print()
print(trainer_two)