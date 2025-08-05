num1=int(input("enter the first number a"))  
num2=int(input("enter the secound number b")) 
num3=int(input("enter the third number c"))  
num4=int(input("Enter the fourth number d"))
if(num1 > num2 and num1 > num3 and num1>num4):  
    print("largest number is num1 ") 
elif(num2>num1 and num2>num3 and num2>num4):
    print("largest number is num2 ")
elif(num3>num1 and num3>num2 and num3> num4):
    print("largest number is num3")

else:
    print("Large number is num4  ")
