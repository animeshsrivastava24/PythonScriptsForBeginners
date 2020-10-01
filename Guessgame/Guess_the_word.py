
#random module to select the random word
#system module to exit the game

from random import randint 
from os import system as sys

#this class contains all the functions required for the game
class master:

	#initialises the game by taking in the words file and storing the options
	def __init__(self):

		f = open('words.txt')
		string = f.read()
		string.strip()
		self.words = string.split('\n')
		self.life = 14


	#this function randomly choses a word from the list of options
	def guess(self):
		
		self.guessedWord = self.words[randint(0,len(self.words))]

	#this function is to take input from the user
	def get(self):

		#userInput = input('Guess a word : ')
		Word = input('Guess a word : ') #userInput[:1]
		return Word.lower()

	
	#This functions allows to play continously 
	def play_again(self):	
		value = input("Do you want to play again ? (y,n) :  ")
		if value == 'y':
			self.start()
		elif value == 'n':
			self.message('stop')
		else:
			print("Wrong input !\n")
			self.play_again()	


	#this function contains a lot of print statements 
	#used to pass some infotmation to the user
	#synax 
	# self.message('argument') : where  argument == 'info' ,'stop', 'won'
	def message(self,arg):

		if arg =='begin':
			print("Welcome to Guess the word game")
			print("1. rules\n2.Start Game")
			num = input("\nEnter an option number : ")
			try:
				num =int(num)
				if num == 1:
					self.message('rules')
				elif num == 2:
					self.message('info')


		if arg == 'rules':
			h = open('rules.txt')
			print(h.read())
			input("\nPress Enter to start!\n")
			h.close()

		#this gives the user some basic hints about the word , like the number of words in it
		elif arg == 'info':
			temp =""
			for x in range(len(self.guessedWord)):
				temp += "-"
			print("Computer have a word in its mind (*memory) you have to guess what is it")
			print("\nThe word have {} ( {} ) letters in it \n".format(temp,len(temp)))
			print("You have got {} attempts left ".format(self.life))

			self.temp = temp



		#this is called when the user correctly guesses the game	
		elif arg == 'won':

			print("\n\nHooray , you have correclty guessed all the letters of the word\n\n")
			print("The word which computer had in mind was ", self.guessedWord)
			self.play_again()


		#this is called when the user loses the game	
		elif arg == 'lost':
			print("Sorry, you didnt guess the word correclty")
			print("The word was ", self.guessedWord)
			self.play_again()
		
		#this is called when the user exits the game
		elif arg == 'stop':
			print("Thank you good bye !")
			sys('exit')



#now this is where , all the game comes together

	def start(self):
		self.message('begin')
		self.life = 12   #no.of guesses the user can make
		self.guess() 	#the computer guesses a word
		user_guessed_correct_letters = ''

		for x in range(len(self.guessedWord.strip())):
			user_guessed_correct_letters += "-" #this is to store the correct charactors entered by the user that matches the guess

		#game starts here
		while self.life > 0:

			#gets the input from the user
			count = 0
			user_char = self.get()

			guess_word = self.guessedWord.strip()


			if len(user_char) > 1:
				if user_char == guess_word:
					self.message('won')
				else:
					print("No your guess is wrong !")
					self.life -= 1
					continue

			elif user_char in guess_word:
				for letter in guess_word:
					if user_char == letter:
						count += 1
				for i in range(len(guess_word)):
					if guess_word[i] == user_char:
						user_guessed_correct_letters[i] = user_char



				print("Yes '{a}' does belong to the word, there are {b} '{a}' in the word ".format(a = user_char,b=count))

				print("Currently word = ",user_guessed_correct_letters)


				


			else:
				print("No '{}' does not belong in the word ".format(user_char))


			if len(user_guessed_correct_letters) == guess_word:
				self.message('won')
			self.life -=1
		self.message('lost')

root = master()
root.start()


 