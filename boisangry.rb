# import random
# import asciiart

guessesTaken = 0
puts('Hello! What is your name?')
myName = gets
number = 1 + rand(50)
puts('Well, ' + myName + ', I am thinking of a number between 1 and 50.')
puts('Take a guess...')
while guessesTaken < 10
    if guessesTaken >= 1
        puts('Try again')
    end
    guess = gets.chomp.to_i
    # try:
    #     guess = int(guess)
    # except ValueError:
    #     puts('Thats not a number numbnuts.')
    #     continue
    guessesTaken += 1
    if guess < 1 or guess > 50
        puts('Your guess is outta range broheimh')
        next
    end
    if guess < number
        puts('Your guess is too low.')
    end
    if guess > number
        puts('Your guess is too high.')
    end
    if guess == number
        break
    end
end
if guess == number
    # guessesTaken = str(guessesTaken)
    # puts(asciiart.win(myName, guessesTaken))
    puts("goodfrickenjob.")
end
if guess != number
    number = number.to_s
    puts('Nope. The number I was thinking of was ' + number)
end
