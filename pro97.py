import random

gameRunning=True
print('___Number Guessing game___')
number=random.randrange(1,11)
lives=5

while lives>0:
    guess=input('guess a number between 1 to 10: ')
    try:
        guess=int(guess)
        if guess<number:
            lives-=1
            print(f'nope, your number is too low\nOnly {lives} lives left')
        elif guess>number:
            lives-=1
            print(f'nope, your number is too high\nOnly {lives} lives left')
        else:
            print(f'You guessed it right!\nthe number was {number}')
            break
            
    except:
        print('invalid input')
if lives==0:
    print('Game over!')
            