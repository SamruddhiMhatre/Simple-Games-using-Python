import random

def guessthenumber():
    random_num = int(random.randint(1,10))
    attempts = 0
    score = 100
    user_res = input('Do you want to play Guess the Number? Enter Yes/No: ')

    while user_res == 'yes' or user_res == 'Yes':
        try:
            num = int(input('Enter a number between 1 and 10: '))
            if num < 1 or num > 10:
                print('Enter the number in given range i.e between 1-10.')

            if num > random_num:
                attempts += 1
                score -= 10
                print('Too high. Your current score is {}'.format(score))

            elif num < random_num:
                attempts += 1
                score -= 10
                print('Too low. Your current score is {}'.format(score))

            elif num == random_num:

                score += 20
                user_res = input('You have guessed the number in {} attempt(s)! Your current score is {}. Do you wish to continue? Yes/No: '.format(attempts, score))
                attempts = 0
                random_num = int(random.randint(1,10))

        except ValueError as err:
                print("Oh no!, that is not a valid value. Try again :)")
                print("({})".format(err))


    if user_res == 'no' or user_res == 'No':
        print('See ya!')
        
        
if __name__ == '__main__':
    guessthenumber()
