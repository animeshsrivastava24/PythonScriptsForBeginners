from random import randint

class game:
	def __init__(self):
		f = open('fruits.txt')
		string = f.read()
		string.strip()
		self.words = string.split('\n')
		self.life = 14

	def guess(self):
		
		self.guessedWord = self.words[randint(0,len(self.words))]
		self.guessedWord_list = [i for i in self.guessedWord]
		self.userGuess_list = ['-' for i in self.guessedWord_list]

	def reveal(self,user_guess):
		if self.user_guess != 'none':
			for i in range(len(self.guessedWord_list)):
				if self.user_guess == self.guessedWord_list[i]:
					self.userGuess_list[i] = self.user_guess

		print('\n Word : ',"".join(self.userGuess_list))


	def check(self):
		if self.user_guess == self.guessedWord or '-' not in self.userGuess_list:
			self.message('won')
		elif self.user_guess[0] in self.guessedWord:
			self.message('true')
		else:
			self.message('false')

	def get(self):

		self.user_guess = input("Enter your guess : ")
		self.check()

	def message(self,arg):

		if arg =='begin':
			print("Welcome Everyone to Guess the Fruit name - game")
			print("1.rules\n2.start game")
			temp = input("Enter the option no (1 / 2): ")
			if temp == '1':
				self.message('rules')
			elif temp == '2':
				self.message('info')
			else:
				print("Error , Try Again\n")
				self.message('begin')

		elif arg == 'true':
			print("\n Your guess was correct\n")
			self.reveal(self.user_guess)

		elif arg == 'false':
			print('\n No your guess was wrong\n')
			self.reveal('none')

		elif arg == 'won':
			print('\n You have guessed the fruit correctly !')
			print('The fruit indeed was : ', self.guessedWord)

		elif arg == 'lost':
			print('\n Better luck next time')
			print('The Fruit which computer had in mind was : ', self.guess_word)
		
		elif arg == 'info':
			temp ='-'*len(self.guessedWord)

			print("Welcome to the Guess Game!\n")
			print("Lets Begin - \n")
			print("Computer have a fruit in its mind (*memory) you have to guess what is it")
			print("The word has {} ( {} ) letters in it".format(temp,len(temp)))
			print('\n')

		elif arg == 'rules':
			h = open('rules.txt')
			print(h.read())
			input("\nPress Enter to start! and ctrl-Z to stop\n")
			h.close()
			self.message('info')

	def start(self):
		self.guess()
		self.message('begin')
		life = self.life

		while life > 0:
			self.get()
			life -= 1
		if life == 0:
			self.message('lost')


root = game()
root.start()





