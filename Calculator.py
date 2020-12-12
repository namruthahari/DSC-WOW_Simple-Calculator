def calculate(response):          #function which calculates and returns the value 
    arg1 = int(input("1st no> "))     
    arg2 = int(input("2nd no> ")) 
    ''' 
    Response codes
    1.Addition
    2.Subtraction
    3.Multiplication
    4.Division
    '''
    if(response == 1):return add(arg1,arg2)
    elif(response == 2):return subtract(arg1,arg2)
    elif (response ==3):return multiply(arg1,arg2)
    elif(response == 4):return divide(arg1,arg2)  
    else:
         print("Invalid resonse in choosing operator  ")
         return 0

'''All math function definitions are listed from here''' 
def add(arg1,arg2): #response code 1
    return arg1+arg2

def subtract(arg1,arg2): #response code 2
    return arg1-arg2

def multiply(arg1,arg2): #response code 3
    return arg1*arg2

def divide(arg1,arg2): #response code 4
    if(arg2 == 0):
        return "Error"
    else:
        return arg1/arg2 
'''Math function definitions end'''        

def calculator():           #function which the user directly interacts with
    print("Welcome to the simple command line calculator \n")
    condition = "y"
    while(condition== 'y'):
         print("Pls enter 1 for addition,2 for subtraction,3 for multiplication,4 for division", end = " ")
         response = int(input("> "))   
         print("Plz enter the numbers to operate")
         print(f"Answer is {calculate(response)}")
         condition = input("Enter y to calculate again:")
    
calculator()   
