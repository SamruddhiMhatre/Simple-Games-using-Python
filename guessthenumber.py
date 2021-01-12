from random import randint

games = int(input("How many games you would like to play? "))

for game in range(games):
    ranNum = int(input("Enter a random number: "))
    value = randint(1,26)
    
    attempts = 0
    
    while ranNum != value:
        if ranNum > value:
            print("Too high!")
            ranNum = int(input("Enter a random number: "))
        elif ranNum < value:
            print("Too low!") 
            ranNum = int(input("Enter a random number: "))
        attempts +=1
    
    print("You have guessed the number in ", attempts , "attempts!")
    