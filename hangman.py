#!/usr/bin/env python3

import random


def rand(file):
    lines = open(file).read().splitlines()
    myline = random.choice(lines)
    return (myline)


wordlist = "./wordlist"
wordtoguess = rand(wordlist)
wordlength = len(wordtoguess)
s = list(wordtoguess)
guess = " "

blank = str('#' * wordlength)
b = list(blank)
tries = 15


def loser():
    lose = """
    __   _______ _   _   _     _____ _____ _____ _ 
    \ \ / /  _  | | | | | |   |  _  /  ___|  ___| |
     \ V /| | | | | | | | |   | | | \ `--.| |__ | |
      \ / | | | | | | | | |   | | | |`--. \  __|| |
      | | \ \_/ / |_| | | |___\ \_/ /\__/ / |___|_|
      \_/  \___/ \___/  \_____/\___/\____/\____/(_)\n\n"""
    return lose

                                        
def winner():
    win = """
    __   _______ _   _   _    _ _____ _   _ _      
    \ \ / /  _  | | | | | |  | |_   _| \ | | |     
     \ V /| | | | | | | | |  | | | | |  \| | |     
      \ / | | | | | | | | |/\| | | | | . ` | |     
      | | \ \_/ / |_| | \  /\  /_| |_| |\  |_|     
      \_/  \___/ \___/   \/  \/ \___/\_| \_(_)\n\n"""
    return win     



def start():
    print(title())
    print("\n" + blank)
    guesses()
    print(loser())
    print("\nYou have lost. The word was '" + wordtoguess + "'.\n")


def guesses():
    global guess
    try:
        guess = input('\nType a letter: ')[0].lower()
    except:
        guesses()
    if guess == "?":
        print(wordtoguess)
        guesses()
    elif guess in wordtoguess:
        index = s.index(guess)
        # print('The index of ' + guess + " is", index)
        b[index] = guess
        print("".join(b))
        if s == b:
            print(winner())
            print("\nYou guessed '" + wordtoguess + "' correctly!\n")
            exit(0)
        else:
            guesses()
    else:
        global tries
        while tries > 1:
            tries -= 1
            print("\nIncorrect. Try Again")
            print("\nYou have " + str(tries) + " left!")
            print("".join(b))
            guesses()


def title():
    s = """ 
     _   _                                         
    | | | |                                        
    | |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    \_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/"""
    return s                             


start()
   
