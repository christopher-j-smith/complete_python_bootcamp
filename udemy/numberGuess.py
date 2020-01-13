#This is a guess the number game from the Automate the Boring Stuff Guy
import random
print('Hello, what is your name?')
name = input()

print(name + ', I am thinking of a number between 1 and 20')
secretNumber = random.randint(1,20)

for i in range(1,7):
    print('Take a guess.')
    try:
        guess = int(input())

        if guess < secretNumber:
            print('Your guess is too low')
        elif guess > secretNumber:
            print('Your guess is too high')
        else:
            break
    except ValueError:
        print('Needs to be a number! That cost you a guess.')

if guess == secretNumber:
    print('Congrats! You guessed the secret number in '+ str(i) + ' guesses.') 
else:
    print('Nope, the number I was thinking of was ' + str(i)


    
