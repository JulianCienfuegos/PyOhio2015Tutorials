class character():
	def __init__(self):
		self.name = 'Malokar Cienfuegos'
		self.alignment = 'good'
		self.armor = 10
		self.HP = 5
		
	def set_name(self, name):
		self.name = name

	def get_name(self):
		return self.name

	def set_alignment(self, align):
		self.alignment = align

	def get_alignment(self):
		return self.alignment

	def set_armor(self, armor):
		self.armor = armor

	def get_armor(self):
		return self.armor

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
			damage = 2
		else:
			damage = 1
		return damage

	def attack(self, roll, opponent):
		if self.can_attack(roll, opponent):
			hp = opponent.get_HP() - self.damage(roll)
			opponent.set_HP(hp)