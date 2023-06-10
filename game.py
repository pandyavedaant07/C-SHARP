#take one input from user
#take ome input from computer
#compare both the inputs
#print the output

import random
choice=["rock", "paper" , "scissor"]
computer=random.choice(choice)
#print(computer)
user=input("choose rock paper or scissor: \n")
if user==computer:
    print("Draw match")
    
#we choose rock
elif user=="rock" and computer=="paper":
    print("you lost") 
elif user=="rock" and computer=="scissor":
    print("you win")

#we choose paper
elif user=="paper" and computer=="rock":
    print("you won")
elif user=="paper" and computer=="scissor":
    print("you lost")
    

#we choose scissor
elif user=="scissor" and computer=="rock":
    print("you lost")
elif user=="scissor" and computer=="paper":
    print("you won")






#user== rock- scissor.     win
      # rock.  paper.       loss
       
    