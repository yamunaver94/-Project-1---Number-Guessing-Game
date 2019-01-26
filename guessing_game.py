"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random
import sys
highscore=[]

def start_game():
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
                print ("You got it! It took you {}".format(tries))
                ans = input("Would you like play again ? [y]es /[n]o: ")
                try:
                    ans = ans.lower()
                    if ans!='n'or ans!='y' :
                        raise ValueError ("Please enter 'y' or 'n'.")
                
                if ans=="n":
                    print("Closing the game see you next time . BYE!!!!")
                    sys.exit()
                elif ans=="y":
                    highscore.append(tries)
                    highscore.sort()
                    print("Get a score under {} to beat the highscore!".format(highscore[0]))
                    tries=0
                    random_no = random.randint(1,10)
                    continue      


                   
if __name__ == '__main__':
    start_game()
