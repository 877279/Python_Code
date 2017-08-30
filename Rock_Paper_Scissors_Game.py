from random import randint

def Rock_Paper_Scissors():
	print('Lets Play Rock,Paper,Scissors!')
	Their_Weapon = input('Choose your Weapon:')
	Their_Weapon = str.lower(Their_Weapon)
	Weapon_Options = ['rock','paper','scissors']
	Random_Number = (randint(0,2))
	Our_Weapon = Weapon_Options[Random_Number]
	print('I Picked {}'.format(Our_Weapon))
	if Our_Weapon == Their_Weapon :
		print('Its a tie!')
	elif Our_Weapon == 'rock' and Their_Weapon == 'paper':
		print('You win!')
	elif Our_Weapon == 'rock' and Their_Weapon == 'scissors':
		print('I win!')
	elif Our_Weapon == 'paper' and Their_Weapon == 'scissors' :
		print('You win!')
	elif Our_Weapon == 'scissors' and Their_Weapon == 'paper':
		print('I win!')
	elif Our_Weapon == 'paper' and Their_Weapon == 'rock':
		print('I win!')
	elif Our_Weapon == 'scissors' and Their_Weapon == 'rock':
		print('You win!')
	else:
		print('Make sure the you spell your weapon correctly!')
	
Rock_Paper_Scissors()

