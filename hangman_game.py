'''hangman game

computer picks a random word, this will then be passed into a variable.
the user will pick a letter, any letter and the computer will check if this letter appears in the chosen word,
if it does it is then marked as a valid letter.
If the chosen letter is not valid or in the chosen word then this chooses a part of the hangman.
the parts of hangman must be derived from ascii code.
The game would then need to display these parts of the hangman as each letter is not part of the word.
'''

import random

from word_list import word_list

hangmanpics = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#words = ["banana", "apple", "pear", "bear", "mouse"] #build a list of words the computer can choose from

guess_word = random.choice(word_list) #using the random function to allow the computer to pick a random word
word_length = len(guess_word) #set the word length for using in the range later
end_of_game = False
lives = 6
display = [] #set a blank list like an array

for i in range(word_length): # for loop to add the number of underscores dependant on the word chosen.
    display += "_" #add the number of underscores dependant on what is in the word chosen by it's length

while not end_of_game: #while the game is not over continue in the loop
    guess = input("Guess a letter: ").lower() #allows user input and forces into lower case

    if guess in display: #if the letter chosen by user is already in the display then print the message you have already guessed this letter.
        print(f"You've already guessed {guess}")

    for position in range(word_length): #this will look across the range using the length of the word, len works out the length, range looks across a word of that length.
        letter = guess_word[position] #assign the guessed word position from the loop into a variable to compare to
        if letter == guess: #if the letter in the loop range i.e any of the letters found during looping through the chosen word matches the user input letter then set the display variable and the position in the list to the same letter chosen by the user.
            display[position] = letter #this sets the display list and the letter position found from the loop to the letter inputted. Position here is like an index, so letter b for example could be in position 0.

    if guess not in guess_word: #if the chosen letter is not in the chosen word by the computer then lose a life and print a message, if all lives are lost then end the game. Lives are deducted from the lives variable.
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}") #add a space in between each letter in the display list.

    if "_" not in display: #if the underscore is not in the display list then end the game as it now knows you have guessed all the letters.
        end_of_game = True
        print("You win.")

    print(hangmanpics[lives]) #print out the index from the hangman variable, so each image is just an index, so losing 5 lives would mean it would look for the 5th entry in the list, or index 4.
