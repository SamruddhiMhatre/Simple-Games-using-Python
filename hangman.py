import random

words = ['earth', 'moon', 'sun', 'mercury','venus', 'mars', 'saturn', 'jupiter', 'uranus', 'neptune', 'pluto']

word = random.choice(words)

response = input('Do you want to play Hangman? yes/no: ')

if response == 'yes':
    guess_count = int(input('Select the number of guesses between 1-10: '))
else:
    print(guess_count)
    print('See ya!')
    

guess_word = ''
    
while guess_count > 0:
    wrong = 0
    
    for char in word:
        if char in guess_word:
            print(char)
        else:
            print('-')
            wrong += 1
    
    if wrong == 0:
        print('You won! The correct word is {}'.format(word))
        break
      
    guess_char = input('Guess the character: ')
    guess_word += guess_char
    
    if guess_char not in word:
        guess_count -= 1
        print('Wrong!You have {} turns left '.format(guess_count))
        
        if guess_count == 0:
            print('You have lost! The correct word is {}'.format(word))
            
    
    
    
    
