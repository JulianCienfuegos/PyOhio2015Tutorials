import unittest
from character import *

class HeroCharactertest(unittest.TestCase):
	def setUp(self):
		self.hero = character()
		self.opponent = character()

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
		default = 10
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
		can_attack = 1
		roll = 10 # 1-20 10 meets the opponents armor class
		self.assertEqual(self.hero.can_attack(roll, self.opponent), can_attack)

	def test_basic_attack(self):
		roll = 19
		old_HP = self.opponent.get_HP()
		self.hero.attack(roll, self.opponent)
		new_HP = self.opponent.get_HP()
		self.assertEqual(old_HP - new_HP, 1)

	def test_critical_attack(self):
		roll = 20
		old_HP = self.opponent.get_HP()
		self.hero.attack(roll, self.opponent)
		new_HP = self.opponent.get_HP()
		self.assertEqual(old_HP - new_HP, 2)

	def test_abilities(self):
		

if __name__ == '__main__':
	unittest.main(exit=False)

		