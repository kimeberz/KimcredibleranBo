import random

guessesTaken = 0
print('Hello! What is your name?')
myName = raw_input()
number = random.randint(1, 50)
print('Well, ' + myName + ', I am thinking of a number between 1 and 50.')
print('Take a guess... Know that I am thinking of a deeper meaning to...')
    if guessesTaken >= 1:
        print('Try again')
    guess = raw_input()
    try:
        guess = int(guess)
    except ValueError:
        print('Thats not a number numbnuts.')
        continue
    guessesTaken += 1
    if guess < 1 or guess > 50:
        print('Your guess is outta range broheimh')
        continue
    if guess < number:
        print('Your guess is too low.')
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!' +
        ''' ,_
          | `""---..._____
          '-...______    _````"""""""'`|
                 \   ```` ``"---...__  |
                 |`              |   ``!
                 |               |     A
                 |               /\   /#\\
                 /`--..______..-'  |  ###
                |   /  `\    /`--. |  ###
               _|  |  .-;`-./;-.  ||  ###
              / \  \ /\_|    |_/\ //\ ##'
              |  `-' \__/ _  \__/ |  |`#
              \_,                 /_/
                 `\              /
                   '.  '.__.'  .'
            jgs      `-,____,-'
                      /"""I""\\
                     /`---'--'\ ''')
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
