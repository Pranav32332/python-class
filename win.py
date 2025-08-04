#win and draw game
import random 
guss=int(input("enter your gussing")) 
number=random.randint(1,10) 
if(guss==number): 
 print("congrulation you win 20 % Discount")  
else: 
  print("Butter luck next time")