# Problem #3
# Write an app for the follwoing two player game. You have a 6 x 6 board. 
# Users take turns rolling the dice twice. first roll is row no, second roll is col number. Mark the spot (row, col) as claimed by the user
# who rolled the dice.
# When the user rolls the dice within 1 col/row of a claimed spot of the other user, the other user gets a point. 
# If the spot is same as the claimed spot of the other user, the user that rolled the dice gets a point. 
# The player who gets 5 points first wins the game.

import random

rows,cols=6,6
arr = [[0 for i in range(cols)] for j in range(rows)]

user1,user2=0,0
def dice(name):
    global user1,user2
    rownum = random.randint(1,6)
    print("row:",rownum-1)
    colnum = random.randint(1,6)
    print("col:",colnum-1)
    
    
    if arr[rownum-1][colnum-1]=="A" or arr[rownum-1][colnum-1]=="R":
        if arr[rownum-1][colnum-1]=="A":
            user1+=1
            print("point user1:",user1)
        else:
            user2+=1
            print("point user2:",user2)
    else:
        arr[rownum-1][colnum-1]=name
    for prn in arr:
        print(prn)
    if user1==5 or user2==5 :
        print(f"----{name}  WIN!!!------")
        return 1
    
while True:
    n=int(input("\n1.user1 to roll dice\n2.user2 to roll dice\n3.exit\n"))
    if n==1:
        if dice("A"):
            break
    elif n==2:
        if dice("R"):
            break
    elif n==3:
        break
    else:
        print("Enter valid number")
        

        
   
    

