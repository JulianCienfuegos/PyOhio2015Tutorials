Solution = '42'

guess = input ('Enter Your Guess: ')
guess = int(guess)
print(guess)

if guess == Solution:
	print('You are a winer!')
	print ('Here is another statement')
else:
	print('You are a non-winner')
	print('so sorry')

print('The game is over')