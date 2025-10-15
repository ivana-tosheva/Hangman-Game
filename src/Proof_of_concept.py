#!
#Ask user if he wants to play!
answer=""
while answer not in ("y","yes","n","no"):
    answer = input("Are you up for a geme? Answer y/yes or n/no: ").lower()
    
    #If user input is yes or just y continue with game
    if answer in( "y", "yes"):
        print("I'll ask  you a couple of questions, and you just give me a simple answer")
        points = 0 #set points to 0
        
        #Question 1, expect user input
        answer1 = input("Is the Earth round? 'y/n' ").lower()
        if answer1 in ("yes", "y"):
            print("Correct, you earned a point!")
            points += 1 #add point
        else:
            print("Not correct, just lost a point")
            if points > 0:
                points -= 1 #loose point
        
        #Question 2
        answer2 = input("Is the sky blue? 'y/n'").lower()
        if answer2 in("yes", "y"):
            print("Correct, you earned a point!")
            points += 1
        else:
            print("Seems blue to me! Lost a point! ")
            if points > 0:
                points -= 1
                
        #Question 3        
        answer3 = input("Can birds fly? 'y/n'").lower()
        if answer3 in ("yes", "y"):
            print(f"Correct, you earned a point! ")
            points += 1
        else:
            print("Wrong, better luck with the next question.")
            if points > 0:
                points -= 1
        
        # Question 4
        answer4 = input("Are cats cute? 'y/n'").lower()
        if answer4 in ("yes", "y"):
            print("Correct, you just earned new point! ")
            points += 1
        else:
            print("No points for cat-haters :)")
            if points > 0:
                points -= 1
        
        #End of Game Print result
        print(f"Game Over! Points earned: {points}/4 ")
    
    #End Game if User enters n or no
    elif answer in ("n", "no"):
        print("OK Have a nice day!")
        break # Break the loop
    
    #Tell user to give a yes/ no answer and go back into loop
    else:
        print("Please answer with y/yes or n/no.")