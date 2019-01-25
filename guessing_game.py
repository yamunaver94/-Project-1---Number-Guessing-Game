"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random
import sys
highest_score=7

def start_game():
    #1. Display an intro/welcome message to the player.
    print ("------------------------------")
    print("Welcome to Number Guessing Game!")
    print ("------------------------------")
    tries=0
    random_no = random.randint(1,10)
    while  True :
        guess=input("Pick a Number between 1 and 10 : ")
        try:
            guess= int (guess)
            if guess<1 or guess>=11 :
                raise ValueError ("Please enter number between 1 and 10(including) !!!!!!!\n TRY AGAIN!!!!")
        except ValueError:
            print("Please enter a NUMBER between 1 - 10.Try Again!!")
        else :
            tries+=1
            if guess > random_no :
                print ("It is lower!")
            elif guess < random_no :
                print("It is higher!")
            elif guess==random_no :
                print "You got it! It took you",tries,"tries"
                ans = input("Would you like play again ? [y]es /[n]o: ")
                ans = ans.lower()
                if ans=="n":
                    print("Closing the game see you next time . BYE!!!!")
                    sys.exit()
                elif ans=="y":
                    print " Highest Score is :",highest_score
                    tries=0
                    random_no = random.randint(1,10)
                    continue         
if __name__ == '__main__':
    start_game()
