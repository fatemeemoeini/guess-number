# user 2input => liw and high bound
# random =>[a,b]
# loop => condition => guess_count=5 => feedback

import random
try:
    low = int(input("Enter lower bound: \n"))
    high = int(input("Enter  high bound :\n"))
except:
    print(" Please enter a valid number ")
r = random.randint(low, high)

guess_count = 5
while guess_count >0:
    try :
        new_guess_str= input (f"remained guess : {guess_count}=> enter your next guess; \n ")
        new_guess = int (new_guess_str)

        if r ==new_guess:
             print("great!your guess is correct")

        elif r > new_guess:

             print("your guess is lower than selected number ")
        else:
             print(" your guess is high than selected number ")

        guess_count-=1
    except:
        print("please enter a valid number ")



























