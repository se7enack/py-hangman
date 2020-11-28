#!/usr/bin/env python3

import random
import animations as ani


def rand(file):
    lines = open(file).read().splitlines()
    myline = random.choice(lines)
    return (myline)

ani.man.reverse()
wordlist = "./wordlist"
wordtoguess = rand(wordlist)
wordlength = len(wordtoguess)
s = list(wordtoguess)
guess = " "

blank = str('#' * wordlength)
b = list(blank)
tries = 7


def start():
    print(ani.title())
    print(ani.man[7])
    print("\n" + blank)
    guesses()
    print(ani.loser())
    print(ani.man[0])
    print("\nYou have lost. The word was '" + wordtoguess + "'.\n")


def guesses():
    global guess
    global tries
    try:
        guess = input('\nType a letter: ')[0].lower()
    except:
        guesses()
    if guess == "?":
        print(wordtoguess)
        guesses()
    elif guess in wordtoguess:
        print(ani.man[tries])
        print("\nCorrect, '" + guess + "' is a letter in this word!\n")
        index = s.index(guess)
        b[index] = guess
        print("".join(b))
        if s == b:
            print(ani.winner())
            print("\nYou guessed '" + wordtoguess + "' correctly!\n")
            exit(0)
        else:
            guesses()
    else:
        while tries > 1:
            tries -= 1
            print(ani.man[tries])
            print("\nIncorrect. Try Again")
            print("\nYou have " + str(tries) + " left!")
            print("".join(b))
            guesses()


start()
   
