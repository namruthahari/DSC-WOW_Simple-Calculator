def calculate(response):  
    arg1 = int(input("1st no> "))     
    arg2 = int(input("2nd no> ")) 
    if(response == 1):return arg1+arg2
    elif(response == 2):return arg1-arg2
    elif (response ==3):return arg1*arg2
    elif(response == 4):return arg1/arg2   
    else:
         print("Invalid resonse in choosing operator  ")
         return 0


def calculator():           
    print("Welcome to the simple command line calculator \n")
    condition = "y"
    while(condition== 'y'):
         print("Pls enter 1 for addition,2 for subtraction,3 for multiplication,4 for division", end = " ")
         response = int(input("> "))   
         print("Plz enter the numbers to operate")
         print(f"Answer is {calculate(response)}")
         condition = input("Enter y to calculate again:")
    
calculator()    