from random import randint

print('enter a number between 1 and 10 and the comptuer will guess your number')

number = 0

while number < 1 or number >10:
    number = int(input('enter a number for the comptuer: '))
    if number > 10:
        print('Number must be lower or equal to 10')
    if number < 1:
        print('Number must be greater than or qual to 1')

    guess = randint(1,10)

    print(' the comptuer take a guess...', guess)

    while guess != number:
        if guess > number:
            guess -= 1 
            guess = randint(1,guess)
        else:
            guess +=1
            guess = randint(guess, 10)
            print('the computer takes a guess...', guess)

    print('the comptuter guessed', guess, 'and it was correct!')