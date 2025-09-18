

# Online Python - IDE, Editor, Compiler, Interpreter

import random
arr = ['rock', 'paper', 'scissors']
rockPaperScissorsInNumberFormat = [0, 1, 2]

flag = True

while flag:
    userInput = input('Enter any number among 0, 1, and 2. To end the game, press 9') #the input entered is in a string format
    userInputInteger = int(userInput)
    if userInputInteger == 9:
        quit()
    elif userInputInteger not in rockPaperScissorsInNumberFormat:
        print('Sorry! I do not recognise that input.')
    else:
        print("User's choice: ",arr[int(userInput)])
        systemGenerated = random.choice(arr)
        print('System chose: ', systemGenerated)
        if arr[userInputInteger] == systemGenerated:
            print('It is a tie!')
            
        # this is to compare rock and paper
        elif arr[userInputInteger] == 'rock' and systemGenerated == 'paper' or arr[userInputInteger] == 'paper' and systemGenerated == 'rock':
            winner = 'paper'
            if arr[userInputInteger] == 'paper':
                print('user wins')
            else:
                print('system wins')
        
        # this is to compare paper and scissors
        elif arr[userInputInteger] == 'paper' and systemGenerated == 'scissors' or arr[userInputInteger] == 'scissors' and systemGenerated == 'paper':
            winner = 'scissors'
            if arr[userInputInteger] == 'scissors':
                print('user wins')
            else:
                print('system wins')
         
         # this is to compare rock and scissors
        elif arr[userInputInteger] == 'rock' and systemGenerated == 'scissors' or arr[userInputInteger] == 'scissors' and systemGenerated == 'rock':
            winner = 'rock'
            if arr[userInputInteger] == 'rock':
                print('user wins')
            else:
                print('system wins')
                
        
            