import random

class Ability:
	def __init__(self, name, attack_strength):
		self.name = name
		self.attack_strength = attack_strength

	def attack(self):
		# Calculate lowest attack value as an integer.
		min_attack = self.attack_strength // (self.attack_strength / 2)
		# Use random.randint(a, b) to select a random attack value.
		attack_strength = random.randint(int(min_attack), self.attack_strength)
		# Return attack value between 0 and the full attack.
		return attack_strength
	
	def update_attack(self, attack_strength):
		self.attack_strength = attack_strength

class Hero:
	def __init__(self, name):
		self.abilities = list() 
		self.name = name 
	
	def add_ability(self, ability):
	# Append ability to self.abilities
		self.abilities.append(ability)

	def attack(self):
	# Call the attack method on every ability in our ability list
	# Add up and return the total of all attacks
		all_attacks = 0

		for ability in self.abilities:

			 all_attacks += Ability.attack(ability)

		return all_attacks

class Weapon(Ability):
	def attack(self, full_attack_value):
		"""
		This method should should return a random value
		between 0 and the full attack power of the weapon.
		Hint: The attack power is inherited.
		"""
		attack_power = random.randint(0, full_attack_value)

class Team:
	def init(self, team_name):
		"""Instantiate resources."""
		self.name = team_name
		self.heroes = list()

	def add_hero(self, Hero):
		"""Add Hero object to heroes list."""
		self.heroes.append(Hero)

	def remove_hero(self, name):
		"""
		Remove hero from heroes list.
		If Hero isn't found return 0.
		"""
		if name == "":
			return 0
		self.heroes.remove(name)

	def find_hero(self, name):
		"""
		Find and return hero from heroes list.
		If Hero isn't found return 0.
		"""
		for hero in self.heroes:
			if name == hero:
				return here
			else:
				return 0
	def view_all_heroes(self):
		"""Print out all heroes to the console."""
		for hero in self.heroes:
			print(hero)

	
if __name__ == "__main__":
	hero = Hero("Wonder Woman")
	print(hero.attack())
	ability = Ability("Divine Speed", 300)
	hero.add_ability(ability)
	print(hero.attack())
	new_ability = Ability("Super Human Strength", 800)
	hero.add_ability(new_ability)
	print(hero.attack())
