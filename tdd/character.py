class armor:
	def __init__ (self):
		self.value = 10 
	
	def get_value(self):
		return self.value
	
	def set_value(self, value):
		self.value = value



class character():
	def __init__(self):
		self.name = 'Malokar Cienfuegos'
		self.alignment = 'good'
		self.HP = 5
		self.abilities = { 'Strength':-100, 'Dexterity':10, 'Constitution':10, 'Wisdom':10, 'Intelligence':10, 'Charisma': 10}
		self.modified_roll = 0
		self.armor = armor()
		armor_value = self.armor.get_value()
		self.armor.set_value(armor_value + self.abilities['Dexterity'])

	def get_modified_roll(self, roll):
		return min(20, roll + self.abilities['Strength']) 

	def get_abilities(self):
		return self.abilities

	def set_name(self, name):
		self.name = name

	def get_name(self):
		return self.name

	def set_alignment(self, align):
		self.alignment = align

	def get_alignment(self):
		return self.alignment

	def set_armor(self, armor):
		self.armor.set_value(armor)

	def get_armor(self):
		return self.armor.get_value()

	def set_HP(self, HP):
		self.HP = HP
	
	def get_HP(self):
		return self.HP

	def can_attack(self, roll, opponent):
		if roll >= opponent.get_armor():
			can_attack = 1
		else:
			can_attack = 0
		return can_attack

	def damage(self, roll):
		if roll == 20:
			damage = max(1,2 + 2*self.abilities['Strength'])
		else:
			damage = max(1,1 + self.abilities['Strength'])
		return damage

	def attack(self, roll, opponent):
		if self.can_attack(roll, opponent):
			hp = opponent.get_HP() - self.damage(roll)
			opponent.set_HP(hp)