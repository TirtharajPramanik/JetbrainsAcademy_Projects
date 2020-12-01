def dash():
    da=''
    for j in random_word:
        if j in k:
            da+=j
        else:
            da+='-'
    print(da)

import random, sys
print('H A N G M A N')


words = ['python', 'java', 'kotlin', 'javascript']
random_word = random.choice(words)
k = ''
l = ''
num = 0
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
n = 0
while n == 0:
    ty = input('Type "play" to play the game, "exit" to quit:')
    if ty == 'exit':
        sys.exit()
    elif ty  == 'play':
        n += 1
    else:
        continue

else:
    while num < 8:
        print()
        dash()
        if len(tuple(k)) == len(tuple(random_word)):
            print('You guessed the word {}!\nYou survived!'.format(random_word))
            break


        letter = input('Input a letter: ')

        if len(letter) != 1:
            print('You should input a single letter')
            continue
        elif letter not in alphabets:
            print('Please enter a lowercase English letter')
            continue
        elif letter in l:
            print('You\'ve already guessed this letter')
            continue
        l += letter
        if letter not in random_word:
            print('That letter doesn\'t appear in the word')
            num += 1
        elif letter in k and letter in random_word:
            print('No improvements')
            num += 1
        else:
            k+=letter
    else:
        print('You lost!')
