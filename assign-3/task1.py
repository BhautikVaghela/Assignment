def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers."
    
    elif num ==0 or num == 1 :
        return 1 
    else :
        result =1
        for i in range(2, num +1):
            result *= i 
        return result 

num = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {num} is {factorial(num)}")