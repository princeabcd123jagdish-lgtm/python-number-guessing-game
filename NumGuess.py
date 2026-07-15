import random
attempts=0
a=random.randint(1,100)
while True:
    attempts+=1
    b=int(input('Enter an integer: '))
    if b==a:
        print(f'Congratulations🎉\nYou guessed the number in {attempts} attempts')
        break
    elif b<a:
        print('Guess  higher')
    else:
        print ('Guess lower')
