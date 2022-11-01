#Guess the number 
import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess the number between 1 and {x}:"))
        if guess < random_number:
            print('Guess higher.')
        elif guess > random_number:
            print('Guess Lower')
    print("You're right.")
x= int(input("Enter the upper limit of the number"))
guess(x)

def computer_guess(y):
    the_number = int(input(f"the number between 1 and {y} you want the computer to guess"))
    guess = random.randint(1,y)
    print('Initial Guess',guess)
    while guess != the_number:
        if guess > the_number:
            guess = random.randint(1,guess)
        elif guess < the_number:
            guess= random.randint(guess,y)
        print('Computers guess', guess)
    print('The computer guessed your number')
    
y=int(input('Enter the upper limit'))
computer_guess(y)
