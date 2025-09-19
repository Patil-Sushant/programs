import random
print('Python program for a word game!')
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)
# print(word)
numOfTries = 3
guesses = ''
while numOfTries > 0:
    guess = input('Enter a character')
    guesses += guess
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end = ' ')
        else:
            print('_')
            failed = failed + 1
    if failed == 0:
        print('You win..')
        print('The word is: ', word)
        break
   
    if guess not in word:
        numOfTries = numOfTries - 1
        if numOfTries == 0:
            print('You lose.')
            print(f'The word was: {word}')
            break
        else:
            print('You have these many turns left: ',numOfTries)
