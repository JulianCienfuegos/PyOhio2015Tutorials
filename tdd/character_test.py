import unittest
from character import *

class HeroCharactertest(unittest.TestCase):
	def setUp(self):
		self.hero = character()
		self.opponent = character()
		self.modifier = {1:-5, 2:-4, 3:-4, 4:-3, 5:-3, 6:-2, 7:-2, 8:-1, 9:-1, 10:0,
						 11:0, 12:1, 13:1, 14:2, 15:3, 16:3, 17:3, 18:4, 19:4, 20:5}

	def test_default_character_name(self):
		self.assertEqual(self.hero.get_name(),'Malokar Cienfuegos')

	def test_default_character_alignment(self):
		g = 'good'
		self.assertEqual(self.hero.get_alignment(), g)
	
	def test_name_mutability(self):
		new_name = 'Juan de los Rios'
		self.hero.set_name(new_name)
		self.assertEqual(self.hero.get_name(),new_name)

	def test_change_character_alignment(self):
		e = 'evil'
		self.hero.set_alignment(e)
		self.assertEqual(self.hero.get_alignment(), e)

	def test_default_armor_class(self):
		default = 20
		self.assertEqual(self.hero.get_armor(), default)

	def test_armor_mutability(self):
		new_armor = 30
		self.hero.set_armor(new_armor)
		self.assertEqual(self.hero.get_armor(), new_armor)

	def test_default_HP(self):
		default = 5
		self.assertEqual(self.hero.get_HP(), default)

	def test_set_HP(self):
		new_HP = 25
		self.hero.set_HP(new_HP)
		self.assertEqual(self.hero.get_HP(), new_HP)

	def test_can_attack(self):
		can_attack = 0
		roll = 10 # 1-20 10 meets the opponents armor class
		self.assertEqual(self.hero.can_attack(roll, self.opponent), can_attack)

	def test_basic_attack(self):
		roll = 1
		damage = self.hero.damage(roll)
		old_HP = self.opponent.get_HP()
		self.hero.attack(roll, self.opponent)
		new_HP = self.opponent.get_HP()
		self.assertEqual(old_HP - new_HP, damage)

	def test_critical_attack(self):
		roll = 20
		damage = self.hero.damage(roll)
		old_HP = self.opponent.get_HP()
		self.hero.attack(roll, self.opponent)
		new_HP = self.opponent.get_HP()
		self.assertEqual(old_HP - new_HP, damage)

	def test_ability_types(self):
		abilities = ['Strength', 'Dexterity', 'Constitution', 'Wisdom', 'Intelligence', 'Charisma']
		character_abilities = self.hero.get_abilities().keys()
		for a in abilities:
			self.assertIn(a, character_abilities)

	def test_strength_modifier_roll(self):
		roll=18
		strength_mod = self.hero.get_abilities()['Strength']
		modified_roll = self.hero.get_modified_roll(roll)
		roll_should_be = min(20, roll + strength_mod)
		self.assertEqual(roll_should_be, modified_roll)

	def test_damage_dealt_basic(self):
		roll = 19
		damage_dealt_basic = self.hero.damage(roll)
		damage_dealt_basic_should = max(1, 1 + self.hero.get_abilities()['Strength'])
		self.assertEqual(damage_dealt_basic, damage_dealt_basic_should)

	def test_damage_dealt_critical(self):
		roll = 20
		damage_dealt_critical = self.hero.damage(roll)
		damage_dealt_critical_should = max(1, 2 + 2*self.hero.get_abilities()['Strength'])
		self.assertEqual(damage_dealt_critical, damage_dealt_critical_should)
#minimum damage is always one even on critical damage
	def test_basic_minimum_damage(self):
		minimum = 1
		roll = 10
		self.assertEqual(minimum, self.hero.damage(roll))

	def test_critical_minimum_damage(self):
		minimum = 1
		roll = 20
		self.assertEqual(minimum, self.hero.damage(roll))

	def test_dexterity_modifier(self):
		default_armor = 10
		armor_should_be = self.hero.get_abilities()['Dexterity'] + default_armor
		armor_is = self.hero.get_armor()
		self.assertEqual(armor_should_be, armor_is)






if __name__ == '__main__':
	unittest.main(exit=False)

		