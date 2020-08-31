# Create a Pokemon class with the __init__() method to keep track of functions.
class Pokemon:
    def __init__(self, name, type, level):
        self.name = name
        self.level = 5
        self.type = type
        self.health = level * 5
        self.max_health = level * 4
        self.is_knocked_out = False

    # Printing name, type, level and health points of Pokemon.
    def __repr__(self):
        return "{name} is a {type} Pokemon type level {level} with {health} health points remaining.".format(name = self.name, type = self.type, level = self.level, health=self.health)

    # Create a variety of methods that changed the variables associated with a Pokemon.
    # lose_health - determines how much health the Pokemon has lost.
    def lose_health(self, healthpoints):
        self.health -= healthpoints
        if self.health <= 0:
            self.health = 0
            self.knock_out()
        else:
            print("{name} now has {health} health.".format(name = self.name, health = self.health))

    # gain_health - determines how much health the Pokemon has gained.
    def gain_health(self, healthpoints):
        if self.health == 0:
            self.revive()
        self.health += healthpoints
        if self.health >= self.max_health:
            self.health = self.max_health
        print("{name} now has {health} health.".format(name = self.name, health = self.health))

    # knock_out - determines when the Pokemon's health has reached 0.
    def knock_out(self):
        self.is_knocked_out = True
        if self.health != 0:
            self.health = 0
        print("{name} is knocked out.".format(name = self.name))

    # The revive() method should only be used if the Pokemon was given some health.
    # If the Pokemon has no health at all, this will be set to 1 once revived. Health for a revived pokemon can't be 0.
    def revive(self):
        self.is_knocked_out = False
        if self.health == 0:
            self.health = 1
        print("{name} is revived.".format(name = self.name))

    # This method takes another Pokémon as an argument and deals damage to that Pokemon. The amount of damage dealt depends on the types of the attacking Pokemon and the Pokemon being attacked. 
    def attack(self, other_pokemon):
    print("\n")
    print("{name} attacks".format(name = self.name))
    if self.type == "Fire":

        # If the attacking Pokemon was at a disadvantage, we dealt damage equal to half the attacking Pokemon’s level.
      if other_pokemon.type == "Water":
        damage = self.level * 0.5
        print("This attack is not very effective.")

        # If the attacking Pokemon has advantage over the other Pokemon, we dealt damage equal to twice the attacking Pokemon’s level.
      elif other_pokemon.type == "Grass":
        damage = self.level * 2
        print("This attack is very effective.")
        
      else:
        damage = self.level
        print("This attack is not effective")
        
    elif self.type == "Water":      
      if other_pokemon.type == "Fire":
        damage = (10 * self.level) * 2
        print(""This attack is very effective.")
        
      elif other_pokemon.type == "Grass":
        damage = (10 * self.level) * 0.5
        print("This attack is not very effective.")
        
      else:
        damage = (10 * self.level)
        print("This attack is not effective")
   
    elif self.type == "Grass":
      if other_pokemon.type == "Fire":
        damage = (10 * self.level) * 0.5
        print("This attack is not very effective.")
        
      elif other_pokemon.type == "Water":
        damage = (10 * self.level) * 2
        print("This attack is very effective.")
        
      else:
        damage = (10 * self.level) 
        print("This attack is not effective.")

    else:
      print("This Pokemon Type Does Not Exist.") 
    other_pokemon.lose_health(damage)

# Create a Trainer class.
class Trainer:
    def __init__(self, name, pokemon_list, num_of_potions):
        self.name = name
        self.pokemons = pokemon_list
        self.potions = num_of_potions
        self.current_pokemon = 0

    # Printing name of the trainer, list of Pokemons and a currently active Pokemon.
    def __repr__(self):
        print("Trainer {name} has: ".format(name = self.name))
        for pokemon in self.pokemons:
            print(pokemon)
        return "Currently active pokemon: {name}".format(name = self.pokemons[self.current_pokemon].name)

    # Using a potion on the currently active Pokemon.
    def use_potion(self):
        if self.potions > 0:
            print("{name} has used a potion.".format(name = self.pokemons[self.current_pokemon].name))
            self.pokemons[self.current_pokemon].gain_health(20)
            self.potions -= 1
            print("Potions left: {potions}.".format(potions = self.potions))
        else:
            print("You have no potions left.")
    
    # Attacking another player.
    def attack_other_trainer(self, other_trainer):
        my_pokemon = self.pokemons[self.current_pokemon]
        their_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
        my_pokemon.attack(their_pokemon)

    # The trainer is able to switch which Pokemon is currently active.
    def switch_active_pokemon(self, new_active_pokemon):
        if new_active_pokemon < len(self.pokemons) and new_active_pokemon >= 0:
            if self.pokemons[new_active_pokemon].is_knocked_out == True:
                print("{name} is knocked out. This Pokemon can't be used".format(name = self.pokemons[new_active_pokemon].name))
            elif new_active_pokemon == self.current_pokemon:
                print("{name} is already in use.".format(name = self.pokemons[new_active_pokemon].name))
            else:
                self.current_pokemon = new_active_pokemon
                print("It is {name}'s turn!".format(name = self.pokemons[self.current_pokemon].name))

# Three classes of Pokemon, one of each type, Charmander (Fire), Squirtle (Water) and Bulbasaur (Grass).
class Charmander(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Charmander", "Fire", level)

class Squirtle(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Squirtle", "Water", level)

class Bulbasaur(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Bulbasaur", "Grass", level)

# List of 6 Pokemons and their levels.
a = Charmander(3)
b = Squirtle(6)
c = Bulbasaur(4)
d = Charmander(9)
e = Squirtle(5)
f = Bulbasaur(8)

# List of trainers, Pokemons owned and number of potions.
trainer_one = Trainer("Ash", [a,b,c], 3)
trainer_two = Trainer("Diantha", [d,e,f], 3)

print(trainer_one)
print(trainer_two)

# Testing commands.
trainer_one.attack_other_trainer(trainer_two)
trainer_two.attack_other_trainer(trainer_one)

trainer_one.use_potion()

trainer_two.switch_active_pokemon(1)